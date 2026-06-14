from pathlib import Path
from backend.llm.nvidia_client import NvidiaClient


class BaseAgent:

    def __init__(self, prompt_file: str):

        self.client = NvidiaClient()

        self.system_prompt = Path(
            prompt_file
        ).read_text()

    def execute(self, task: str):

        prompt = f"""
{self.system_prompt}

Task:
{task}
"""

        return self.client.generate(prompt)