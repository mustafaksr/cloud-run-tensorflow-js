provider "google" {
  project = var.project_id
  region  = var.region
}


resource "google_cloud_run_service" "default" {
  name     = "tf-js-regression"
  location = var.region
  provider = google-beta
  metadata {
    annotations = {
      "run.googleapis.com/launch-stage" = "BETA"
    }
  }

  template {
    spec {
      containers {
        image = "gcr.io/civic-access-350318/cloudruntensorflowjs:latest"
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
data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location    = google_cloud_run_service.default.location
  project     = google_cloud_run_service.default.project
  service     = google_cloud_run_service.default.name

  policy_data = data.google_iam_policy.noauth.policy_data
}