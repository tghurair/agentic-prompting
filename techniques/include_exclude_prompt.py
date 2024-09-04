from prompt_technique import PromptTechnique
from typing import Dict, Any, List

class IncludeExcludePrompt(PromptTechnique):
    def generate(self, prompt: str, include: List[str] = None, exclude: List[str] = None) -> Dict[str, Any]:
        include = include or []
        exclude = exclude or []
        system_prompt = """You are a helpful assistant that generates include-exclude prompts. Your task is to take the user's input and generate a prompt that specifies elements to include and exclude in the response.
        
        Format your response using the following structure:
        
        <PROMPT>
        [Restate the original prompt]
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
        
        prompt_content = self._extract_content(response, "PROMPT")
        include_content = self._extract_content(response, "INCLUDE")
        exclude_content = self._extract_content(response, "EXCLUDE")
        task_content = self._extract_content(response, "TASK")
        
        return {
            "prompt": prompt_content,
            "additional_info": {
                "include": include_content,
                "exclude": exclude_content,
                "task": task_content
            }
        }