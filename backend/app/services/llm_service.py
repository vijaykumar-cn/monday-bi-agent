from openai import OpenAI
from app.config import NVIDIA_API_KEY


class LLMService:
    def __init__(self):
        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=NVIDIA_API_KEY,
            timeout=180,
        )

    def ask(self, prompt: str):
        completion = self.client.chat.completions.create(
            model="meta/llama-3.2-3b-instruct",  # Changed here
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.2,
            max_tokens=256,
        )

        return completion.choices[0].message.content