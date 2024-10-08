from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any, List

class IncludeExcludePrompt(PromptTechnique):
    def generate(self, prompt: str, include: List[str] = None, exclude: List[str] = None) -> Dict[str, Any]:
        include = include or []
        exclude = exclude or []
        system_prompt = """You are a helpful assistant that generates include-exclude prompts. Your task is to take the user's input and generate a prompt that specifies elements to include and exclude in the response.
        
        Format your response using the following structure:
        
        <PROMPT>
        [Enhance and expand on the original prompt while adhering on the main scope of the prompt, focusing on the core question or task. Maintain its original scope and intent, providing additional context or clarification if necessary.]
        </PROMPT>
        
        <INCLUDE>
        [List elements to include, with brief explanations]
        </INCLUDE>
        
        <EXCLUDE>
        [List elements to exclude, with brief explanations]
        </EXCLUDE>
        
        <TASK>
        [Provide instructions on how to respond to the prompt while adhering to the include/exclude guidelines]
        </TASK>"""
        
        user_prompt = f"Generate an include-exclude prompt based on the following input: {prompt}\n\nInclude: {', '.join(include)}\nExclude: {', '.join(exclude)}. Feel free to add include/exclude examples but ensure that they are still relevant to the scope of each section."
        response = self._call_api(system_prompt, user_prompt)
        return response.strip()
        