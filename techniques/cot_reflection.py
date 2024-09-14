from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any

class ChainOfThoughtReflection(PromptTechnique):
    def generate(self, prompt: str) -> Dict[str, Any]:
        system_prompt = """You are an AI assistant that generates Chain of Thought (CoT) prompts with reflection. Your task is to take the user's input and create a prompt that encourages step-by-step reasoning followed by reflection on that reasoning. Use the following structure:

        <PROMPT>
        [Expanded version of the original prompt, encouraging step-by-step reasoning]
        </PROMPT>

        <INSTRUCTIONS>
        1. Think through the problem step by step within the <thinking> tags.
        2. Reflect on your thinking to check for any errors or improvements within the <reflection> tags.
        3. Make any necessary adjustments based on your reflection.
        4. Provide your final, concise answer within the <output> tags.

        Important: The <thinking> and <reflection> sections are for your internal reasoning process only. 
        Do not include any part of the final answer in these sections. 
        The actual response to the query must be entirely contained within the <output> tags.
        </INSTRUCTIONS>

        <OUTPUT_FORMAT>
        <thinking>
        [Your step-by-step reasoning goes here. This is your internal thought process, not the final answer.]
        <reflection>
        [Your reflection on your reasoning, checking for errors or improvements]
        </reflection>
        [Any adjustments to your thinking based on your reflection]
        </thinking>
        <output>
        [Your final, concise answer to the query. This is the only part that will be shown to the user.]
        </output>
        </OUTPUT_FORMAT>
        """
        
        user_prompt = f"Generate a Chain of Thought prompt with reflection based on the following input: {prompt}"
        response = self._call_api(system_prompt, user_prompt)
        
        #prompt_content = self._extract_content(response, "PROMPT")
        #instructions_content = self._extract_content(response, "INSTRUCTIONS")
        #output_format_content = self._extract_content(response, "OUTPUT_FORMAT")
        
        return response