# infra/gateway.tf
variable "gateway_name" {
  type = string
  default = "ai-gateway"
}

resource "aws_lb" "gateway" {
  name               = var.gateway_name
  internal           = true
  load_balancer_type = "application"
  subnets            = module.vpc.private_subnets
}

resource "aws_lb_listener" "https" {
  load_balancer_arn = aws_lb.gateway.arn
  port              = 443
  protocol          = "HTTPS"

  default_action {
    type = "fixed-response"
    fixed_response {
      content_type  = "application/json"
      message_body = "{\"status\": \"ok\"}"
    }
  }
}