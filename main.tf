provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_cloud_run_service" "example" {
  name     = "tf-js-regression"
  location = var.region

  template {
    spec {
      containers {
        image = "mustafakeser/cloudruntensorflowjs:latest"
        startup_probe {
            tcp_socket {
                port = 3000
            }
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}