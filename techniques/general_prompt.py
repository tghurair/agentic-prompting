from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any

class GeneralPrompt(PromptTechnique):
    def generate(self, prompt: str) -> Dict[str, Any]:
        system_prompt = """You are a helpful assistant that generates prompts. Your task is to take the user's input and generate a clear, expanded prompt while adhering to the original scope. 
        
        Format your response using the following structure:
        
        <PROMPT>
        [Your generated prompt goes here]
        </PROMPT>
        """
        
        user_prompt = f"Please generate a clear and expanded prompt based on the following input: {prompt}"
        response = self._call_api(system_prompt, user_prompt)
        
        prompt_content = self._extract_content(response, "PROMPT")
        
        return {
            "prompt": prompt_content
        }