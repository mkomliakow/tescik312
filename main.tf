terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=4.1.0"
    }
  }
}
provider "azurerm" {
  features {}
  resource_provider_registrations = "none"
}

terraform {
  backend "azurerm" {
    resource_group_name  = "rg-MichalK"
    storage_account_name = "stmichalk"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

resource "azurerm_service_plan" "example" {
  name                = "michal-app-service-plan"
  location            = "westeurope"
  resource_group_name = "rg-MichalK"
  os_type             = "Linux"
  sku_name            = "P0v3"
}


resource "azurerm_linux_web_app" "example" {
  name                = "michal-webapp-t2s-wkshp-1"
  location            = "westeurope"
  resource_group_name = "rg-MichalK"
  service_plan_id     = azurerm_service_plan.example.id
  site_config {}
}
