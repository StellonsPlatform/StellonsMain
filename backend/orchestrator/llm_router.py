import json

from backend.llm.nvidia_client import NvidiaClient
from backend.models.router_response import RouterResponse


class LLMRouter:

    def __init__(self):

        self.client = NvidiaClient()

        with open(
            "backend/llm/prompts/router_prompt.md",
            "r",
            encoding="utf-8",
        ) as file:

            self.router_prompt = file.read()

    def route(
        self,
        task: str,
    ) -> RouterResponse:

        print(
            f"[LLM ROUTER] Routing task: {task}"
        )

        response = self.client.generate(
            system_prompt=self.router_prompt,
            user_prompt=task,
        )

        print(
            f"[LLM ROUTER] Raw response: {response}"
        )

        try:

            data = json.loads(response)

            return RouterResponse(
                agent=data["agent"],
                confidence=float(
                    data["confidence"]
                ),
                reasoning=data["reasoning"],
            )

        except Exception as e:

            print(
                f"[LLM ROUTER] Failed to parse response: {e}"
            )

            return RouterResponse(
                agent="PlannerAgent",
                confidence=0.0,
                reasoning="Router parsing failure",
            )