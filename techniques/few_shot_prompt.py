from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any
from openai import OpenAI

class FewShotPrompt(PromptTechnique):
    def __init__(self, client: OpenAI):
        super().__init__(client)

    def generate(self, prompt: str, num_examples: int = 3) -> Dict[str, Any]:
        system_prompt = f"""You are a helpful assistant that generates few-shot prompts. Your task is to take the user's input and generate a prompt that includes {num_examples} relevant examples to guide the response.
        
        Format your response using the following structure:
        
        <PROMPT>
        [Restate the original prompt and provide a clear and concise explanation of the task, you may expand on it but dont go outside the scope of the original prompt, include any necessary context or instructions, expand on the prompt to provide more clarity if needed, but do not go outside the scope of the original prompt]
        </PROMPT>
        
        <EXAMPLES>
        [Provide {num_examples} concise, relevant examples related to the prompt]
        </EXAMPLES>
        
        <TASK>
        [Provide instructions on how to respond to the original prompt using insights from the examples]
        </TASK>
        
       <OUTPUT_FORMAT>
        Task: [blank]
        </OUTPUT_FORMAT>"""
        
        user_prompt = f"Generate a few-shot prompt with {num_examples} relevant examples based on the following input: {prompt}"
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