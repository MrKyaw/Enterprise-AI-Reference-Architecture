# infra/outputs.tf
output "gateway_endpoint" {
  value = aws_lb.gateway.dns_name
  description = "Public DNS name for AI Gateway (internal only)"
}

output "vpc_cidr" {
  value = module.vpc.vpc_cidr
  description = "VPC CIDR block"
}