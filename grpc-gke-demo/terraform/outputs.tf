output "cloud_run_url" {
  value = google_cloud_run_service.grpc_api.status[0].url
}
