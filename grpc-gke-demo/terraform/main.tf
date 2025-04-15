resource "google_cloud_run_service" "grpc_api" {
  name     = "grpc-api"
  location = var.region

  template {
    spec {
      containers {
        image = var.image
        ports {
          container_port = 8080
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Grant public access to the Cloud Run service
resource "google_cloud_run_service_iam_binding" "public_access" {
  location = google_cloud_run_service.grpc_api.location
  project  = google_cloud_run_service.grpc_api.project
  service  = google_cloud_run_service.grpc_api.name
  role     = "roles/run.invoker"
  members  = ["allUsers"]
}
