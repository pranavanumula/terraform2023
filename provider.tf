terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.73.1"
    }
  }
}

provider "google" {
    project = "global-axe-391317"
    region = "us-central1"
    zone = "us-central1-a"
}