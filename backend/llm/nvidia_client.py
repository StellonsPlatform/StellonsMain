import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class NvidiaClient:

    def __init__(self):

        self.client = OpenAI(
            api_key=os.getenv("NVIDIA_API_KEY"),
            base_url="https://integrate.api.nvidia.com/v1"
        )

    def generate(
        self,
        prompt: str,
        model="meta/llama-3.1-8b-instruct"
    ):

        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print("Calling NVIDIA...")

        return response.choices[0].message.content