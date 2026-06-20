from backend.models.cloud_sku import (
    CloudSKU,
)


class SKUCatalogService:

    def get_skus(self):

        return [

            CloudSKU(
                cloud="azure",
                service="AKS",
                sku_name="Standard",
                category="Kubernetes",
                available=True,
            ),

            CloudSKU(
                cloud="azure",
                service="AKS",
                sku_name="Premium",
                category="Kubernetes",
                available=True,
            ),

            CloudSKU(
                cloud="azure",
                service="Virtual Machine",
                sku_name="Standard_D4s_v5",
                category="Compute",
                available=True,
            ),

            CloudSKU(
                cloud="azure",
                service="Storage Account",
                sku_name="Standard_GZRS",
                category="Storage",
                available=True,
            ),

            CloudSKU(
                cloud="azure",
                service="Azure SQL",
                sku_name="Business Critical",
                category="Database",
                available=True,
            ),
        ]

    def find_sku(
        self,
        sku_name: str,
    ):

        for sku in self.get_skus():

            if (
                sku.sku_name.lower()
                ==
                sku_name.lower()
            ):

                return sku

        return None