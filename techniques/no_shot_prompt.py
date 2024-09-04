from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any

class NoShotPrompt(PromptTechnique):
    def generate(self, prompt: str) -> Dict[str, Any]:
        system_prompt = """You are an AI assistant that generates no-shot prompts. Transform and expand the user's input and but scope driven prompt without adding information outside its scope. Follow this structure:

        <PROMPT>
        [Expanded version of the original prompt, staying strictly within its scope]
        </PROMPT>

        <INSTRUCTIONS>
        [Clear, step-by-step instructions for completing the task]
        </INSTRUCTIONS>

        <INPUT_EXAMPLE>
        [A brief example of the expected input]
        </INPUT_EXAMPLE>

        <OUTPUT_FORMAT>
        [Exact output format as specified by the task, typically a single line for the answer. Dont provide an an actual output the input example, explain how the outputs should be]
        </OUTPUT_FORMAT>

        Ensure the output format asks for a single answer without explanation or reasoning. The instructions should specify to answer the question directly and concisely.
        """
        
        user_prompt = f"Transform this prompt into a comprehensive no-shot prompt: {prompt}"
        
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