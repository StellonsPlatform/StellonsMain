from fastapi.testclient import TestClient

from backend.api.main import app

client = TestClient(app)

response = client.post(
    "/terraform/export",
    json={
        "goal": """
        Deploy production AKS cluster
        in India Central
        with 10 nodes
        Premium Tier
        GZRS
        Sidecar Support
        """
    },
)

print()
print("=" * 60)
print("V0.4.17 EXPORT METADATA")
print("=" * 60)
print()

print(
    response.json()
)