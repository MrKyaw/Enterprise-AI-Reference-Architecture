terraform {
  required_version = ">= 1.6.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.6"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "project" {
  type    = string
  default = "rag-starter-kit"
}

variable "environment" {
  type    = string
  default = "dev"
}

variable "tags" {
  type    = map(string)
  default = {}
}

resource "random_id" "suffix" {
  byte_length = 3
}

locals {
  name = "${var.project}-${var.environment}-${random_id.suffix.hex}"
  tags = merge(
    {
      Project     = var.project
      Environment = var.environment
      ManagedBy   = "terraform"
    },
    var.tags
  )
}

resource "aws_kms_key" "artifacts" {
  description         = "Artifact encryption key for ${local.name}"
  enable_key_rotation = true
  tags                = local.tags
}

resource "aws_s3_bucket" "artifacts" {
  bucket = "${local.name}-artifacts"
  tags   = local.tags
}

resource "aws_s3_bucket_versioning" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm     = "aws:kms"
      kms_master_key_id = aws_kms_key.artifacts.arn
    }
  }
}

resource "aws_s3_bucket_public_access_block" "artifacts" {
  bucket                  = aws_s3_bucket.artifacts.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_lifecycle_configuration" "artifacts" {
  bucket = aws_s3_bucket.artifacts.id
  rule {
    id     = "expire-noncurrent"
    status = "Enabled"
    filter {}
    noncurrent_version_expiration {
      noncurrent_days = 90
    }
  }
}

resource "aws_cloudwatch_log_group" "app" {
  name              = "/aws/rag-starter-kit/${var.environment}"
  retention_in_days = 30
  tags              = local.tags
}

output "artifact_bucket" {
  value = aws_s3_bucket.artifacts.bucket
}

output "kms_key_arn" {
  value = aws_kms_key.artifacts.arn
}

output "log_group_name" {
  value = aws_cloudwatch_log_group.app.name
}
