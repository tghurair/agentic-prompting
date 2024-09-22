from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any

class ChainOfThoughtReflection(PromptTechnique):
    def generate(self, prompt: str) -> Dict[str, Any]:
        system_prompt = """You are an prompt engineer that generates effective prompts for a model to follow.
<INSTRUCTIONS>
- Expand on vague ideas with reasonable assumptions
- Should specify the role in the beginning of the prompt
- Provide clear instructions and considerations for the model in the prompt
- Specify any output format or structure requirements the user would like to see
- Ensure your enhanced prompt maintains the original intent and scope while providing a more comprehensive and actionable version.
- Clear and concise instructions should be provided in the prompt.
</INSTRUCTIONS>
Make Sure to follow the following structure in your response:
<OUTPUT_FORMAT>
<PROMPT>
[Expanded version of the original prompt, encouraging step-by-step reasoning]
</PROMPT>
</OUTPUT_FORMAT>
"""
        reflection_prompt = """<INSTRUCTIONS>
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
</OUTPUT_FORMAT>"""
        user_prompt = f"{prompt}"
        response = self._call_api(system_prompt, user_prompt)
        
        #prompt_content = self._extract_content(response, "PROMPT")
        #instructions_content = self._extract_content(response, "INSTRUCTIONS")
        output_format_content = self._extract_content(response, "OUTPUT_FORMAT")
        
        return f"{output_format_content.strip()} \n\n {reflection_prompt.strip()}".strip()