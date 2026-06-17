from backend.services.infrastructure_aggregator import (
    InfrastructureAggregator,
)

aggregator = InfrastructureAggregator()

context = aggregator.aggregate(
    goal="Deploy AKS cluster in East US with 3 nodes",
    tasks=[
        "Create Resource Group",
        "Create Service Principal",
        "Create AKS Cluster",
        "Verify AKS Cluster",
    ],
)

print()
print("===================================")
print("INFRASTRUCTURE CONTEXT")
print("===================================")

print(context.model_dump())