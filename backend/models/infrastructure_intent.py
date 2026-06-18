from pydantic import BaseModel


class InfrastructureIntent(BaseModel):

    cloud: str

    resource_type: str

    region: str

    node_count: int

    environment: str

    monitoring: bool

    cluster_count: int = 1

    sku_tier: str = "standard"

    redundancy: str = "none"

    sidecar_support: bool = False

    def normalize(self):

        #
        # Default cloud
        #

        if not self.cloud.strip():

            self.cloud = "azure"

        #
        # Default resource type
        #

        if not self.resource_type.strip():

            self.resource_type = "aks"

        #
        # Default region
        #

        if not self.region.strip():

            self.region = "East US"

        #
        # Default environment
        #

        if not self.environment.strip():

            self.environment = "production"

        #
        # Minimum production nodes
        #

        if (
            self.environment.lower()
            == "production"
            and self.node_count < 3
        ):

            self.node_count = 3

        #
        # Minimum cluster count
        #

        if self.cluster_count < 1:

            self.cluster_count = 1

        #
        # SKU validation
        #

        valid_skus = [
            "standard",
            "premium",
        ]

        if (
            not self.sku_tier.strip()
            or self.sku_tier.lower()
            not in valid_skus
        ):

            self.sku_tier = "standard"

        #
        # Redundancy validation
        #

        valid_redundancy = [
            "none",
            "lrs",
            "zrs",
            "gzrs",
        ]

        if (
            not self.redundancy.strip()
            or self.redundancy.lower()
            not in valid_redundancy
        ):

            self.redundancy = "none"

        return self