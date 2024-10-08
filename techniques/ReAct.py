from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any

class ReActPrompt(PromptTechnique):
    def generate(self, prompt: str, tool: str = None) -> str:
        system_prompt = """You are an expert prompt engineer specializing in generating prompts that combine reasoning and actions. Your goal is to help guide a language model through reasoning while simultaneously specifying task-specific actions.

<INSTRUCTIONS>
- Expand on vague ideas with reasonable assumptions.
- Specify the role in the beginning of the prompt.
- Provide clear reasoning steps followed by an appropriate action for each step.
- Ensure that the reasoning and the subsequent action are clearly separated and logically connected.
- Specify any output format or structure requirements the user would like to see.
- Maintain the original intent and scope of the prompt while providing a more comprehensive and actionable version.
- Ensure clarity, conciseness, and adaptability in the problem-solving approach.
- If a specific tool is provided, incorporate it into the actions where appropriate.
</INSTRUCTIONS>

Make sure to follow the following structure in your response:
<OUTPUT_FORMAT>
<PROMPT>
[Expanded version of the original prompt, incorporating the tool if provided]
</PROMPT>

<REASONING_AND_ACTION>
<REASONING>
[Provide clear, step-by-step reasoning related to the original prompt.]
</REASONING>
<ACTION>
[Specify the action the language model should take based on the reasoning provided. If a tool is specified, incorporate it into the action.]
</ACTION>
</REASONING_AND_ACTION>
</OUTPUT_FORMAT>
"""

        user_prompt = f"Generate a ReAct prompt based on the following input: {prompt}"
        if tool:
            user_prompt += f"\n\nTool to incorporate: {tool}"
        response = self._call_api(system_prompt, user_prompt)
        output_format_content = self._extract_content(response, "OUTPUT_FORMAT")
        return output_format_content.strip()