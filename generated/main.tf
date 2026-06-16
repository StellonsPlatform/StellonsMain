
terraform {
  required_version = ">= 1.6.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}



resource "azurerm_resource_group" "main" {
  name     = "rg-${var.environment}"
  location = var.region
}

resource "azurerm_kubernetes_cluster" "main" {

  count = 1

  name                = "aks-${var.environment}-${count.index}"

  location            = azurerm_resource_group.main.location

  resource_group_name = azurerm_resource_group.main.name

  dns_prefix = "aks${var.environment}"

  default_node_pool {
    name       = "system"
    node_count = var.node_count
    vm_size    = "Standard_D4s_v5"
  }


  sku_tier = "Premium"


  identity {
    type = "SystemAssigned"
  }


  service_mesh_profile {
    mode = "Istio"
  }


}


