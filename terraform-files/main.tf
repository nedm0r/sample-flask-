terraform {
  backend "gcs" {
    bucket = "bucket-1093-terraform"
    prefix = "terraform/state"
  }
}

variable "gcp_credentials" {
  description = "Path to the GCP service account key file"
  type        = string
  default     = file("var.gcp_credentials")  # Replace with the actual path to your service account key file
}

provider "google" {
  project     = var.gcp_project_id
  region      = var.gcp_region
  
}

resource "google_container_cluster" "gke_cluster" {
  name               = var.gke_cluster_name
  location           = var.gke_zones[0]
  initial_node_count = 1

  node_config {
    machine_type = var.gke_machine_type
    disk_size_gb = 50
    disk_type    = "pd-balanced"
  }
}

output "cluster_endpoint" {
  value = google_container_cluster.gke_cluster.endpoint
}

output "cluster_ca_certificate" {
  value     = google_container_cluster.gke_cluster.master_auth.0.cluster_ca_certificate
  sensitive = true
}

resource "google_compute_firewall" "allow_inbound" {
  name    = "allow-inbound"
  network = "default"

  # Правила для входящего трафика
  allow {
    protocol = "tcp"
    ports    = ["22", "5000", "80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]
}

resource "google_compute_firewall" "allow_outbound" {
  name    = "allow-outbound"
  network = "default"

  # Правила для исходящего трафика
  allow {
    protocol = "icmp"
  }
  allow {
    protocol = "tcp"
  }
  allow {
    protocol = "udp"
  }

  source_ranges = ["0.0.0.0/0"]
}
