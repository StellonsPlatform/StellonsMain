from backend.services.cloud_catalog_service import (
    CloudCatalogService,
)

service = CloudCatalogService()

services = service.get_services()

regions = service.get_regions()

print()
print("=" * 60)
print("V0.7.0 CLOUD KNOWLEDGE LAYER")
print("=" * 60)
print()

print("SERVICES")
print()

for item in services:

    print(
        item.model_dump()
    )

print()

print("REGIONS")
print()

for item in regions:

    print(
        item.model_dump()
    )