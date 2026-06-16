from backend.models.infrastructure_request import (
    InfrastructureRequest,
)
from backend.models.generator_response import (
    GeneratorResponse,
)


class TerraformGenerator:

    def generate(
        self,
        request: InfrastructureRequest,
    ) -> GeneratorResponse:

        # =====================================
        # AKS GENERATION
        # =====================================

        if (
            request.cloud.lower() == "azure"
            and request.resource_type.lower() == "aks"
        ):

            terraform_code = f'''
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

resource "azurerm_resource_group" "main" {{
  name     = "rg-aks-prod"
  location = "{request.region}"
}}

resource "azurerm_kubernetes_cluster" "main" {{
  name                = "aks-prod"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  dns_prefix = "aksprod"

  default_node_pool {{
    name       = "system"
    node_count = {request.node_count}
    vm_size    = "Standard_D4s_v5"
  }}

  identity {{
    type = "SystemAssigned"
  }}
}}
'''

            return GeneratorResponse(
                tool="terraform",
                code=terraform_code,
            )

        # =====================================
        # DEFAULT
        # =====================================

        return GeneratorResponse(
            tool="terraform",
            code="# Unsupported infrastructure request",
        )