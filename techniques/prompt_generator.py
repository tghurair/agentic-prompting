from typing import Dict, Any
from openai import OpenAI
from general_prompt import GeneralPrompt
from no_shot_prompt import NoShotPrompt
from few_shot_prompt import FewShotPrompt
from include_exclude_prompt import IncludeExcludePrompt

class PromptGenerator:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.techniques = {
            "general": GeneralPrompt(self.client),
            "no_shot": NoShotPrompt(self.client),
            "few_shot": FewShotPrompt(self.client),
            "include_exclude": IncludeExcludePrompt(self.client)
        }

    def generate_prompt(self, original_prompt: str, technique: str = "general", **kwargs) -> Dict[str, Any]:
        if technique not in self.techniques:
            raise ValueError(f"Unknown technique: {technique}")
        
        prompt_technique = self.techniques[technique]
        result = prompt_technique.generate(original_prompt, **kwargs)
        
        return {
            "original_prompt": original_prompt,
            "technique": technique,
            "transformed_prompt": result["prompt"],
            "additional_info": result.get("additional_info", {})
        }

# Usage example
if __name__ == "__main__":
    import os
    
    api_key = os.getenv('OPENAI_API_KEY')
    generator = PromptGenerator(api_key)
    
    # Test a single technique
    technique = "no_shot"  # Change this to test a different technique
    print(f"\nTesting {technique} technique:")
    result = generator.generate_prompt("provide a sentiment analysis prompt for arabic tweets(saudi)", 
                                           technique=technique )
    
    print(result)
    