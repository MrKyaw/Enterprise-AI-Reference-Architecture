# infra/main.tf
terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# VPC with gateway endpoint
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  name    = "inference-vpc"
  cidr    = "10.0.0.0/16"
  azs     = ["us-east-1a", "us-east-1b"]
}

# AI Gateway endpoint (private endpoint only)
module "gateway" {
  source = "terraform-aws-modules/alb/aws"
  name   = "ai-gateway"
  internal = true
}

# Outputs
output "gateway_endpoint" {
  value = module.gateway.private_dns_name
  description = "Private DNS name for AI Gateway"
}