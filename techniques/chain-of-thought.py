from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any

class ChainOfThoughtPrompt(PromptTechnique):
    def generate(self, prompt: str) -> Dict[str, Any]:
        system_prompt = """You are an AI assistant that generates chain-of-thought prompts. Transform the user's input into a structured prompt that encourages step-by-step reasoning. Follow this structure:

        <PROMPT>
        [Restate and expand on the original prompt, focusing on the core question or task. Maintain its original scope and intent, providing additional context or clarification if necessary.]
        </PROMPT>

        <INSTRUCTIONS>
        Problem-Solving Chain of Thought 
        • Define the Problem: Identify the core issue. Use curiosity to explore what needs solving.
        • Understand the Context: Examine the surrounding environment or situation for insights.
        • Collect Evidence: Gather relevant data using available resources and observations.
        • Formulate Solutions: Brainstorm multiple potential approaches, considering pros and cons.
        • Test Solutions: Experiment with different approaches, learning from successes and failures.
        • Reflect and Adjust: Review outcomes and refine your approach as needed.
        • Repeat as Necessary: Continue iterating until a viable solution is found.

        Keep in Mind 
        • Avoid overcomplication; sometimes the simplest solution is best.
        • Stay focused and minimize distractions from irrelevant information.
        • Practice patience and persistence when facing challenges.
        </INSTRUCTIONS>

        <REASONING_TEMPLATE>
        [Provide a flexible template for the reasoning process, allowing for iteration and adjustment as needed. Include placeholders for defining the problem, understanding context, collecting evidence, formulating and testing solutions, and reflecting on outcomes.]
        </REASONING_TEMPLATE>

        <OUTPUT_FORMAT>
        [Specify the desired format for the final answer, emphasizing clarity and conciseness while allowing for explanation of the problem-solving process if relevant.]
        </OUTPUT_FORMAT>

        Ensure the instructions encourage clear, logical thinking and adaptability in the problem-solving approach."""

        user_prompt = f"Transform this prompt into a chain-of-thought prompt: {prompt}"
        
        response = self._call_api(system_prompt, user_prompt)
        
        prompt_content = self._extract_content(response, "PROMPT")
        instructions_content = self._extract_content(response, "INSTRUCTIONS")
        reasoning_template_content = self._extract_content(response, "REASONING_TEMPLATE")
        output_format_content = self._extract_content(response, "OUTPUT_FORMAT")
        
        return f"""
            Prompt:
            {prompt_content}

            Instructions:
            {instructions_content}

            Reasoning Template:
            {reasoning_template_content}

            Output Format:
            {output_format_content}
            """
