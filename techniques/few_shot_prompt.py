from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any
from openai import OpenAI

class FewShotPrompt(PromptTechnique):
    def __init__(self, client: OpenAI):
        super().__init__(client)

    def generate(self, prompt: str, num_examples: int = 3) -> Dict[str, Any]:
        system_prompt = f"""You are an expert prompt enginner that generates comprehensive few-shot prompts. Your task is to take the user's input, which may range from a simple idea to a detailed request, and create a prompt that specifies elements to include and exclude in the response.
       
        <INSTRUCTIONS>
        - Expand on vague ideas with reasonable assumptions
        - Should specify the role in the beginning of the prompt
        - Provide clear instructions and considerations for the model in the prompt
        - Specify any output format or structure requirements the user would like to see
        - Ensure your enhanced prompt maintains the original intent and scope while providing a more comprehensive and actionable version.
        - Clear and concise instructions should be provided in the prompt.
        </INSTRUCTIONS>

        Make sure to follow the following structure:
        <OUTPUT_FORMAT>
        <PROMPT>
        [Expanded and detailed version of the original prompt. If the original is vague, flesh it out with reasonable assumptions. If it's already detailed, refine and clarify it further.]
        </PROMPT>

        <INSTRUCTIONS>
        [Clear, step-by-step instructions for completing the task, including how to use the examples. Break down complex tasks into smaller steps.]
        </INSTRUCTIONS>

        <EXAMPLES>
        [Provide {num_examples} relevant examples. Each example should have an Input and Output. Ensure examples cover a range of complexity and scenarios.]
        </EXAMPLES>
        </OUTPUT_FORMAT>
        Ensure the output format asks for a single answer without explanation or reasoning, unless the task specifically requires elaboration. The instructions should specify to answer the question directly and concisely, using the provided examples as a guide."""

        user_prompt = f"""{prompt}"""

        response = self._call_api(system_prompt, user_prompt)

        output_format = self._extract_content(response, "OUTPUT_FORMAT")
        return output_format.strip()

