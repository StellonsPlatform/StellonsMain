import os

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


class NvidiaClient:

    def __init__(self):

        api_key = os.getenv("NVIDIA_API_KEY")

        if not api_key:
            raise ValueError(
                "NVIDIA_API_KEY not found in environment variables."
            )

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://integrate.api.nvidia.com/v1",
        )

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        model: str = "meta/llama-3.1-8b-instruct",
        temperature: float = 0.1,
        max_tokens: int = 512,
    ) -> str:

        try:

            print(
                f"[NVIDIA] Calling model: {model}"
            )

            response = (
                self.client.chat.completions.create(
                    model=model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt,
                        },
                        {
                            "role": "user",
                            "content": user_prompt,
                        },
                    ],
                )
            )

            return (
                response
                .choices[0]
                .message
                .content
                .strip()
            )

        except Exception as e:

            print(
                f"[NVIDIA ERROR] {str(e)}"
            )

            raise