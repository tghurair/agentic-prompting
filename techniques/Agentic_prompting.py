from techniques.prompt_technique import PromptTechnique
from typing import Dict, Any
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from crewai_tools import BaseTool

class GeneralPromptTool(BaseTool):
    name: str = "General Prompt"
    description: str = "Generate a general prompt based on the given idea."

    def _run(self, idea: str) -> str:
        return f"""Based on the idea: {idea}, please provide a general prompt, Format your response using the following structure (Treat this as a template do not output it as is):
                
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

class NoShotPromptTool(BaseTool):
    name: str = "No-Shot Prompt"
    description: str = "Generate a no-shot prompt based on the given idea."

    def _run(self, idea: str) -> str:
        return f"""Based on the idea: {idea}, please provide a no-shot prompt, Format your response using the following structure (Treat this as a template do not output it as is):
        
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
        </TASK>
        """

class FewShotPromptTool(BaseTool):
    name: str = "Few-Shot Prompt"
    description: str = "Generate a few-shot prompt based on the given idea."

    def _run(self, idea: str) -> str:
        return f"""Based on the idea: {idea}, please provide a few-shot prompt, Format your response using the following structure (Treat this as a template do not output it as is):
        <INSTRUCTIONS>
        - Expand on vague ideas with reasonable assumptions
        - Should specify the role in the beginning of the prompt
        - Provide clear instructions and considerations for the model in the prompt
        - Specify any output format or structure requirements the user would like to see
        - Ensure your enhanced prompt maintains the original intent and scope while providing a more comprehensive and actionable version.
        - Clear and concise instructions should be provided in the prompt.
        </INSTRUCTIONS>

        Make sure to follow the following structure:
        <OUTPUT_FORMAT>
        <PROMPT>
        [Expanded and detailed version of the original prompt. If the original is vague, flesh it out with reasonable assumptions. If it's already detailed, refine and clarify it further.]
        </PROMPT>

        <INSTRUCTIONS>
        [Clear, step-by-step instructions for completing the task, including how to use the examples. Break down complex tasks into smaller steps.]
        </INSTRUCTIONS>

        <EXAMPLES>
        [Provide as many relevant examples neccessary. Each example should have an Input and Output. Ensure examples cover a range of complexity and scenarios. the range should be 2-5 examples]
        </EXAMPLES>
        
        </OUTPUT_FORMAT>
        Ensure the output format asks for a single answer without explanation or reasoning, unless the task specifically requires elaboration. The instructions should specify to answer the question directly and concisely, using the provided examples as a guide
        </OUTPUT_FORMAT>
        """

class IncludeExcludePromptTool(BaseTool):
    name: str = "Include-Exclude Prompt"
    description: str = "Generate an include-exclude prompt based on the given idea."

    def _run(self, idea: str) -> str:
        return f"""Based on the idea: {idea}, please provide an include-exclude prompt, Format your response using the following structure (Treat this as a template do not output it as is):
        
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
        </TASK>
        """

class ChainOfThoughtPromptTool(BaseTool):
    name: str = "Chain-of-Thought Prompt"
    description: str = "Generate a chain-of-thought prompt based on the given idea."

    def _run(self, idea: str) -> str:
        return f"""Based on the idea: {idea}, please provide a chain-of-thought prompt, Format your response using the following structure (Treat this as a template. do not output it as is):
        
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

        Ensure the instructions encourage clear, logical thinking and adaptability in the problem-solving approach.
        """

class CoTReflectionPromptTool(BaseTool):
    name: str = "CoT Reflection Prompt"
    description: str = "Generate a chain-of-thought prompt with reflection based on the given idea."

    def _run(self, idea: str) -> str:
        return f"""Based on the idea: {idea}, please provide a chain-of-thought prompt with reflection, Format your response using the following structure (Treat this as a template do not output it as is):

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

        reflection prompt structure:
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
        </OUTPUT_FORMAT>"""

class AgenticPrompting(PromptTechnique):
    def __init__(self, client):
        super().__init__(client)
        self.llm = ChatOpenAI(
            model="gpt-4",
            api_key=client.api_key
        )

    def generate(self, prompt: str) -> Dict[str, Any]:
        prompt_engineer = Agent(
            role='Prompt Engineer',
            goal='Enhance and optimize prompts iteratively to improve LLM performance.',
            backstory=(
                "You are a seasoned Prompt Engineer with deep expertise in natural language processing. "
                "Your primary skill is in fine-tuning prompts to maximize clarity, relevance, and effectiveness. "
                "You have a systematic approach to testing and refining prompts to achieve the best outcomes."
            ),
            memory=True,
            verbose=True,
            llm=self.llm,
            max_iter=6
        )

        analyze_prompt_task = Task(
            description=(
                "Analyze the given prompt and choose the most suitable prompt technique for the task. "
                "Consider aspects such as clarity, relevance, and potential ambiguities. "
                "Provide a detailed explanation for each identified issue, referencing best practices in prompt engineering. "
                "Recommend the most appropriate prompt technique (general prompt, no shot prompt, few shot prompt, include exclude prompt, chain of thought prompt, chain of thought prompt with reflection) and justify your choice.\n\n"
                f"Prompt: {prompt}\n\n"
                "Your analysis should be thorough and actionable, offering specific suggestions for enhancing the prompt and selecting the best technique."
            ),
            expected_output='A comprehensive analysis of the prompt with detailed explanations, actionable suggestions for improvement, and a Decision for the most suitable prompt technique.',
            agent=prompt_engineer
        )

        generate_prompt_task = Task(
            description=(
                "Generate a detailed and comprehensive prompt based on the analysis done, "
                "ensuring clarity, relevance, and adherence to the guidelines provided."
                "Implement the recommended prompt technique"
                "Do Not go out of the scope of the prompt, ensure that the main scope is adhered to and we are not wandering off."
                "Output the prompt only"
            ),
            expected_output='Enhanced prompt that follows the decision made for which prompt technique to use',
            agent=prompt_engineer,
            tools=[
                GeneralPromptTool(),
                NoShotPromptTool(),
                FewShotPromptTool(),
                IncludeExcludePromptTool(),
                ChainOfThoughtPromptTool(),
                CoTReflectionPromptTool()
            ]
        )

        crew = Crew(
            agents=[prompt_engineer],
            tasks=[analyze_prompt_task, generate_prompt_task],
            verbose=True
        )

        result = crew.kickoff({'prompt': prompt})
        
        return {
            "prompt": result.tasks_output[-1].raw,
            "analysis": result.tasks_output[0].raw
        }
        