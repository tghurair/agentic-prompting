from abc import ABC, abstractmethod
from typing import Dict, Any
from openai import OpenAI

class PromptTechnique(ABC):
    def __init__(self, client: OpenAI):
        self.client = client

    @abstractmethod
    def generate(self, prompt: str) -> Dict[str, Any]:
        pass

    def _call_api(self, system_prompt: str, user_prompt: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        return completion.choices[0].message.content

    def _extract_content(self, text: str, tag: str) -> str:
        start_tag = f"<{tag}>"
        end_tag = f"</{tag}>"
        start = text.find(start_tag) + len(start_tag)
        end = text.find(end_tag)
        return text[start:end].strip()