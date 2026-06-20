from backend.models.service_availability import (
    ServiceAvailability,
)


class AvailabilityService:

    def get_availability(self):

        return [

            ServiceAvailability(
                cloud="azure",
                service="AKS",
                region="East US",
                available=True,
                sku="Premium",
            ),

            ServiceAvailability(
                cloud="azure",
                service="AKS",
                region="India Central",
                available=True,
                sku="Premium",
            ),

            ServiceAvailability(
                cloud="azure",
                service="AKS",
                region="West Europe",
                available=True,
                sku="Standard",
            ),

            ServiceAvailability(
                cloud="azure",
                service="Azure SQL",
                region="East US",
                available=True,
                sku="Business Critical",
            ),

            ServiceAvailability(
                cloud="azure",
                service="Storage",
                region="India Central",
                available=True,
                sku="Standard_GZRS",
            ),
        ]

    def find(
        self,
        service: str,
        region: str,
    ):

        for item in self.get_availability():

            if (
                item.service.lower()
                == service.lower()
                and
                item.region.lower()
                == region.lower()
            ):

                return item

        return None