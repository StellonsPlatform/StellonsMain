from fastapi.testclient import TestClient

from backend.api.main import app

client = TestClient(app)

response = client.post(
    "/terraform/export",
    json={
        "goal": """
Create 2 AKS clusters

10 nodes

Premium tier

India Central

GZRS redundancy

Sidecar support
"""
    },
)

print()
print("=" * 60)
print("V0.4.13 EXPORT API")
print("=" * 60)
print()

print(
    response.json()
)