from backend.llm.nvidia_client import NvidiaClient

client = NvidiaClient()

response = client.generate(
    "Say hello from DeepSeek."
)

print(response)