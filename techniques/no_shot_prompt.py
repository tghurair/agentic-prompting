from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any

class NoShotPrompt(PromptTechnique):
    def generate(self, prompt: str) -> Dict[str, Any]:
        system_prompt = """You are a prompt engineer specializing in generating comprehensive no-shot prompts. Your task is to transform and expand the user's input, regardless of its initial detail level, into a well-structured, thorough prompt.:

        
        <INSTRUCTIONS>
        - Expand on vague ideas with reasonable assumptions
        - Should specify the role in the beginning of the prompt
        - Provide clear instructions and considerations for the model in the prompt
        - Specify any output format or structure requirements the user would like to see
        - Ensure your enhanced prompt maintains the original intent and scope while providing a more comprehensive and actionable version.
        - Clear and concise instructions should be provided in the prompt.
        </INSTRUCTIONS>

        Make sure to follow the following format:

        <OUTPUT_FORMAT>
        <PROMPT>
        [Expanded and detailed version of the original prompt. If the original is vague, flesh it out with reasonable assumptions. If it's already detailed, refine and organize it.]
        </PROMPT>

        <INSTRUCTIONS>
        [Clear, step-by-step instructions for completing the task. Break down complex tasks into smaller, manageable steps.]
        </INSTRUCTIONS>

        </OUTPUT_FORMAT>
        """
        
        user_prompt = f"Transform this input into a comprehensive no-shot prompt, expanding or refining as necessary: {prompt}"
        
        response = self._call_api(system_prompt, user_prompt)
        
        # Extract content for each section
        output_format_content = self._extract_content(response, "OUTPUT_FORMAT")
        
        return output_format_content.strip()
