from fastapi.testclient import (
    TestClient,
)

from backend.api.main import app

client = TestClient(app)

response = client.post(
    "/terraform/export",
    json={
        "goal": """
        Create Premium AKS

        India Central

        10 nodes
        """
    },
)

print()
print("=" * 60)
print("V0.4.18 COST ESTIMATION")
print("=" * 60)
print()

print(
    response.json()
)