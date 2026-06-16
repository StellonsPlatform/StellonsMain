from fastapi.testclient import TestClient

from backend.api.main import app

client = TestClient(app)

response = client.post(
    "/terraform",
    json={
        "goal": """
Deploy production AKS cluster
with monitoring
in East US
and 5 nodes
"""
    },
)

print()
print("=" * 60)
print("V0.4.7 TERRAFORM API")
print("=" * 60)

print()

print(
    response.json()
)