variable "gcp_credentials"{
    type=string
    description = "Location of service account for GCP"
}

variable "gcp_project_id"{
    type=string
    description = "GCP Progect id"
}

variable "gcp_region"{
    type=string
    description = "GCP region"
}

variable "gke_cluster_name"{
    type=string
    description = "GKE cluster name"
}


variable "gke_zones"{
    type=list(string)
    description = "GKE zone list"
}

variable "gke_node_name"{
    type=string
    description = "GKE Cluster name"
}

variable "gke_machine_type"{
    type=string
    description = "GKE machine type"
}

variable "gcp_bucket_name"{
    type=string
    description = "GCP bucket name"
}
