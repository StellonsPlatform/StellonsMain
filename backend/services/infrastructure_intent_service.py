import json

from backend.llm.nvidia_client import NvidiaClient

from backend.models.infrastructure_intent import (
    InfrastructureIntent,
)


class InfrastructureIntentService:

    def __init__(self):

        self.client = NvidiaClient()

        with open(
            "backend/llm/prompts/infrastructure_prompt.md",
            "r",
            encoding="utf-8",
        ) as file:

            self.system_prompt = file.read()

    def extract(
        self,
        goal: str,
    ) -> InfrastructureIntent:

        response = self.client.generate(
            system_prompt=self.system_prompt,
            user_prompt=goal,
        )

        print(
            f"[INFRASTRUCTURE INTENT] Raw Response:\n{response}"
        )

        try:

            data = json.loads(response)

            intent = InfrastructureIntent(
                cloud=data["cloud"],
                resource_type=data["resource_type"],
                region=data["region"],
                node_count=int(
                    data["node_count"]
                ),
                environment=data["environment"],
                monitoring=bool(
                    data["monitoring"]
                ),
                cluster_count=int(
                    data.get(
                        "cluster_count",
                        1,
                    )
                ),
                sku_tier=data.get(
                    "sku_tier",
                    "standard",
                ),
                redundancy=data.get(
                    "redundancy",
                    "none",
                ),
                sidecar_support=bool(
                    data.get(
                        "sidecar_support",
                        False,
                    )
                ),
            )

            return intent.normalize()

        except Exception as e:

            print(
                f"[INTENT PARSE ERROR] {e}"
            )

            return InfrastructureIntent(
                cloud="azure",
                resource_type="aks",
                region="East US",
                node_count=3,
                environment="production",
                monitoring=False,
                cluster_count=1,
                sku_tier="standard",
                redundancy="none",
                sidecar_support=False,
            ).normalize()