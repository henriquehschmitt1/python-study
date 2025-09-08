terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

provider "local" {}

resource "local_file" "example" {
  filename = "example.txt"       # path of the file to create
  content  = "Hello, Terraform!\nThis is a local file."
}
