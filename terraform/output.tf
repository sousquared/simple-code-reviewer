output "domain" {
  description = "デプロイされたアプリケーションのドメイン名"
  value       = var.domain
}

output "lb_ip" {
  description = "load balancerのIP"
  value       = google_compute_global_address.simple_code_reviewer_lb_ip.address
}

output "url" {
  description = "アプリケーションのURL"
  value       = "https://${var.domain}"
}

output "certificate_status" {
  description = "SSL証明書のステータス"
  value = {
    id = data.google_compute_ssl_certificate.simple_code_reviewer_cert.certificate_id
    creation_timestamp = data.google_compute_ssl_certificate.simple_code_reviewer_cert.creation_timestamp
    expire_time = data.google_compute_ssl_certificate.simple_code_reviewer_cert.expire_time
  }
}
