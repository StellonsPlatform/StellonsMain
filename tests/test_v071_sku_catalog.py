from backend.services.sku_catalog_service import (
    SKUCatalogService,
)

service = SKUCatalogService()

print()
print("=" * 60)
print("V0.7.1 SKU CATALOG")
print("=" * 60)
print()

print("AVAILABLE SKUS")
print()

for sku in service.get_skus():

    print(
        sku.model_dump()
    )

print()

print("LOOKUP")
print()

result = service.find_sku(
    "Standard_D4s_v5"
)

if result:

    print(
        result.model_dump()
    )