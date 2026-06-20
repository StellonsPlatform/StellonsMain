from backend.models.cloud_service import (
    CloudService,
)

from backend.models.cloud_region import (
    CloudRegion,
)


class CloudCatalogService:

    def get_services(self):

        return [

            CloudService(
                cloud="azure",
                service_name="Azure Kubernetes Service",
                resource_type="aks",
                supported_regions=[
                    "East US",
                    "West Europe",
                    "India Central",
                ],
            ),

            CloudService(
                cloud="azure",
                service_name="Azure SQL",
                resource_type="sql",
                supported_regions=[
                    "East US",
                    "India Central",
                ],
            ),

        ]

    def get_regions(self):

        return [

            CloudRegion(
                cloud="azure",
                region="East US",
                status="available",
            ),

            CloudRegion(
                cloud="azure",
                region="India Central",
                status="available",
            ),

            CloudRegion(
                cloud="azure",
                region="West Europe",
                status="available",
            ),

        ]