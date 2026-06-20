from backend.models.cloud_provider import (
    CloudProvider,
)


class ProviderCatalogService:

    def get_providers(self):

        return [

            CloudProvider(
                provider_name="azurerm",
                version="4.0",
                cloud="azure",
                supported_services=[
                    "aks",
                    "vm",
                    "storage",
                    "sql",
                ],
            ),

            CloudProvider(
                provider_name="aws",
                version="6.0",
                cloud="aws",
                supported_services=[
                    "eks",
                    "ec2",
                    "rds",
                ],
            ),

            CloudProvider(
                provider_name="google",
                version="6.0",
                cloud="gcp",
                supported_services=[
                    "gke",
                    "compute",
                    "sql",
                ],
            ),

            CloudProvider(
                provider_name="kubernetes",
                version="2.0",
                cloud="multi-cloud",
                supported_services=[
                    "deployment",
                    "service",
                    "ingress",
                ],
            ),
        ]

    def find_provider(
        self,
        provider_name: str,
    ):

        for provider in self.get_providers():

            if (
                provider.provider_name.lower()
                ==
                provider_name.lower()
            ):

                return provider

        return None