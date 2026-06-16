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

        if (
            self.environment.lower()
            == "production"
            and self.node_count < 3
        ):
            self.node_count = 3

        if self.cluster_count < 1:
            self.cluster_count = 1

        valid_skus = [
            "standard",
            "premium",
        ]

        if (
            self.sku_tier.lower()
            not in valid_skus
        ):
            self.sku_tier = "standard"

        valid_redundancy = [
            "none",
            "lrs",
            "zrs",
            "gzrs",
        ]

        if (
            self.redundancy.lower()
            not in valid_redundancy
        ):
            self.redundancy = "none"

        return self