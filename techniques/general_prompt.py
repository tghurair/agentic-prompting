from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any

class GeneralPrompt(PromptTechnique):
    def generate(self, prompt: str) -> Dict[str, Any]:
        system_prompt = """You are an expert prompt enginner specializing in enhancing and expanding user prompts. Your task is to take the user's input which would be an idea or incomplete propmt to use for their AI model.

        <INSTRUCTIONS>
        - Expand on vague ideas with reasonable assumptions
        - Should specify the role in the beginning of the prompt
        - Provide clear instructions and considerations for the model in the prompt
        - Specify any output format or structure requirements the user would like to see
        - Ensure your enhanced prompt maintains the original intent and scope while providing a more comprehensive and actionable version.
        - Clear and concise instructions should be provided in the prompt.
        </INSTRUCTIONS>
        
        <OUTPUT_FORMAT>
        - The output should be clear and well instructed prompt that the user can use for their AI model.
        </OUTPUT_FORMAT>
        """

        user_prompt = prompt

        response = self._call_api(system_prompt, user_prompt)
        
        # Since we're only returning a single prompt, we don't need to extract multiple sections
        return response.strip()