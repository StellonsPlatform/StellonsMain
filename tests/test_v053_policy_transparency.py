from fastapi.testclient import (
    TestClient,
)

from backend.api.main import app

client = TestClient(app)

response = client.post(
    "/terraform/export",
    json={
        "goal": """
        Production AKS Cluster

        East US

        Premium

        5 Nodes
        """
    },
)

print()
print("=" * 60)
print("V0.5.3 POLICY TRANSPARENCY")
print("=" * 60)
print()

print(
    response.json()
)