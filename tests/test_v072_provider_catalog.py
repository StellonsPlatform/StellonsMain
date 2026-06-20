from backend.services.provider_catalog_service import (
    ProviderCatalogService,
)

service = ProviderCatalogService()

print()
print("=" * 60)
print("V0.7.2 PROVIDER CATALOG")
print("=" * 60)
print()

print("PROVIDERS")
print()

for provider in service.get_providers():

    print(
        provider.model_dump()
    )

print()

print("LOOKUP")
print()

provider = service.find_provider(
    "azurerm"
)

if provider:

    print(
        provider.model_dump()
    )