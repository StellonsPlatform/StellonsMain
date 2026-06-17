from pathlib import Path

from backend.llm.nvidia_client import (
    NvidiaClient,
)


class BaseAgent:

    def __init__(
        self,
        prompt_file: str,
    ):

        self.client = NvidiaClient()

        self.system_prompt = Path(
            prompt_file
        ).read_text(
            encoding="utf-8"
        )

    def execute(
        self,
        task: str,
    ):

        return self.client.generate(
            system_prompt=self.system_prompt,
            user_prompt=task,
        )