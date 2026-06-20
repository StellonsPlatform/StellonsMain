from backend.services.availability_service import (
    AvailabilityService,
)

service = AvailabilityService()

print()
print("=" * 60)
print("V0.7.3 AVAILABILITY MATRIX")
print("=" * 60)
print()

print("AVAILABILITY")
print()

for item in service.get_availability():

    print(
        item.model_dump()
    )

print()

print("LOOKUP")
print()

result = service.find(
    "AKS",
    "India Central",
)

if result:

    print(
        result.model_dump()
    )