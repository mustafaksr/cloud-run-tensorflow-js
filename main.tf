provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_cloud_run_service" "example" {
  name     = "example"
  location = var.region

  template {
    spec {
      containers {
        image = "mustafakeser/cloudruntensorflowjs:latest"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}