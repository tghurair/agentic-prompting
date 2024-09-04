from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any

class NoShotPrompt(PromptTechnique):
    def generate(self, prompt: str) -> Dict[str, Any]:
        system_prompt = """You are a helpful assistant that generates no-shot prompts. Your task is to take the user's input and generate a prompt that doesn't rely on examples or prior knowledge, focusing solely on the given task.
        
        Format your response using the following structure:
        
        <PROMPT>
        [Your generated no-shot prompt goes here, ensure that it is a valid prompt , explain the task in a way that is clear manner without going out of the scope of the task. Describe the expected format or structure of the input]
        </PROMPT>
        
        <INSTRUCTIONS>
        [Provide clear, step-by-step instructions for completing the task]
        </INSTRUCTIONS>
        
        <INPUT_EXAMPLE>
        [Provide an example input of what is to be expected, an actual input that the model will recieve]
        </INPUT_EXAMPLE>
        
        <OUTPUT_FORMAT>
        Task:
        </OUTPUT_FORMAT>"""
        
        user_prompt = f"Generate a no-shot prompt based on the following input, ensuring it doesn't rely on examples or prior knowledge: {prompt}"
        response = self._call_api(system_prompt, user_prompt)
        
        prompt_content = self._extract_content(response, "PROMPT")
        instructions_content = self._extract_content(response, "INSTRUCTIONS")
        output_format_content = self._extract_content(response, "OUTPUT_FORMAT")
        
        return {
            "prompt": prompt_content,
            "additional_info": {
                "instructions": instructions_content,
                "output_format": output_format_content
            }
        }