from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any
from openai import OpenAI

class FewShotPrompt(PromptTechnique):
    def __init__(self, client: OpenAI):
        super().__init__(client)

    def generate(self, prompt: str, num_examples: int = 3) -> Dict[str, Any]:
        system_prompt = f"""You are an AI assistant that generates few-shot prompts. Transform the user's input into a concise, focused prompt with {num_examples} relevant examples. Follow this structure:

        <PROMPT>
        [Expanded version of the original prompt, staying strictly within its scope]
        </PROMPT>

        <INSTRUCTIONS>
        [Clear step-by-step instructions for completing the task, including how to use the examples]
        </INSTRUCTIONS>

        <EXAMPLES>
        [Provide {num_examples} relevant examples. Each example should have an Input and Output.]
        </EXAMPLES>

        <INPUT_EXAMPLE>
        [A brief example of what the actual input will look like]
        </INPUT_EXAMPLE>

        <OUTPUT_FORMAT>
        [Exact output format as specified by the task, typically a single line for the answer. Dont provide an an actual output the input example, explain how the outputs should be]
        </OUTPUT_FORMAT>

        Ensure the output format asks for a single answer without explanation or reasoning. The instructions should specify to answer the question directly and concisely, using the provided examples as a guide."""

        user_prompt = f"Transform this prompt into a few-shot prompt with {num_examples} relevant examples, staying strictly within its scope: {prompt}. The output format should ask for a single answer without explanation."
        response = self._call_api(system_prompt, user_prompt)
        
        prompt_content = self._extract_content(response, "PROMPT")
        examples_content = self._extract_content(response, "EXAMPLES")
        task_content = self._extract_content(response, "TASK")
        
        return {
            f"""
            Prompt:
            {prompt_content}

            Examples:
            {examples_content}

            Task:
            {task_content}
            """
        }