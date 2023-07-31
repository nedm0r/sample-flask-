provider "google" {
  credentials = file(var.gcp_credentials)
  project     = var.gcp_project_id
  region = var.gcp_region
}

resource "google_container_cluster" "gke_cluster" {
  name               = var.gke_cluster_name
  location           = var.gke_zones[0]
  initial_node_count = 1

 node_config {
    machine_type   = var.gke_machine_type
    disk_size_gb   = 50
    disk_type      = "pd-balanced"
    
  }
}

output "cluster_endpoint" {
  value = google_container_cluster.gke_cluster.endpoint
}

output "cluster_ca_certificate" {
  value     = google_container_cluster.gke_cluster.master_auth.0.cluster_ca_certificate
  sensitive = true
}

resource "google_storage_bucket" "my_bucket" {
  name          = var.gcp_bucket_name  
  location      = var.gcp_region           
  force_destroy = true                     

  versioning {
    enabled = false 
  }
}
