from backend.models.infrastructure_request import (
    InfrastructureRequest,
)

from backend.models.terraform_project import (
    TerraformProject,
)


class TerraformGenerator:

    def generate(
        self,
        request: InfrastructureRequest,
    ) -> TerraformProject:

        monitoring_block = ""

        if request.monitoring:

            monitoring_block = """
resource "azurerm_log_analytics_workspace" "main" {
  name                = "law-${var.environment}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  sku                 = "PerGB2018"
}
"""

        premium_block = ""

        if request.sku_tier.lower() == "premium":

            premium_block = """
  sku_tier = "Premium"
"""

        sidecar_block = ""

        if request.sidecar_support:

            sidecar_block = """
  service_mesh_profile {
    mode = "Istio"
  }
"""

        redundancy_comment = ""

        if request.redundancy.lower() == "gzrs":

            redundancy_comment = """
# Requested redundancy: GZRS
# Storage resources should use Standard_GZRS
"""

        main_tf = f"""
terraform {{
  required_version = ">= 1.6.0"

  required_providers {{
    azurerm = {{
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }}
  }}
}}

provider "azurerm" {{
  features {{}}
}}

{redundancy_comment}

resource "azurerm_resource_group" "main" {{
  name     = "rg-${{var.environment}}"
  location = var.region
}}

resource "azurerm_kubernetes_cluster" "main" {{

  count = {request.cluster_count}

  name                = "aks-${{var.environment}}-${{count.index}}"

  location            = azurerm_resource_group.main.location

  resource_group_name = azurerm_resource_group.main.name

  dns_prefix = "aks${{var.environment}}"

  default_node_pool {{
    name       = "system"
    node_count = var.node_count
    vm_size    = "Standard_D4s_v5"
  }}

{premium_block}

  identity {{
    type = "SystemAssigned"
  }}

{sidecar_block}

}}

{monitoring_block}
"""

        variables_tf = """
variable "environment" {
  type = string
}

variable "region" {
  type = string
}

variable "node_count" {
  type = number
}
"""

        outputs_tf = """
output "resource_group_name" {
  value = azurerm_resource_group.main.name
}

output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.main.name
}
"""

        terraform_tfvars = f'''
environment = "{request.environment}"

region = "{request.region}"

node_count = {request.node_count}
'''

        return TerraformProject(
            main_tf=main_tf,
            variables_tf=variables_tf,
            outputs_tf=outputs_tf,
            terraform_tfvars=terraform_tfvars,
        )