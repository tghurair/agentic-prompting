import json
import os
from openai import OpenAI

class PromptGenerator:
    def __init__(self):
        # Set up OpenAI client
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        self.client = OpenAI(api_key=api_key)

        self.techniques = {
            "general": self.general_prompt,
            "no_shot": self.no_shot_prompting,
            "few_shot": self.few_shot_prompting,
            "include_exclude": self.include_exclude_prompting,
        }

    def generate_prompt(self, original_prompt, technique="general", **kwargs):
        """
        Generate a transformed prompt using ChatGPT based on the selected technique.

        Args:
            original_prompt (str): The original user prompt.
            technique (str): The prompting technique to use.
            **kwargs: Additional arguments that might be required by specific techniques.

        Returns:
            dict: A dictionary containing the original and transformed prompts.
        """
        system_prompt, user_prompt = self.techniques[technique](original_prompt, **kwargs)
        
        completion = self.client.chat.completions.create(
            model="gpt-4",  
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )

        transformed_prompt = completion.choices[0].message.content

        return {
            "original_prompt": original_prompt,
            "technique": technique,
            "transformed_prompt": transformed_prompt
        }

    def general_prompt(self, prompt):
        system_prompt = """You are a helpful assistant that generates prompts. Your task is to take the user's input and generate a clear, expanded prompt while adhering to the original scope. 
        
        Format your response using the following structure:
        
        <PROMPT>
        [Your generated prompt goes here]
        </PROMPT>
        
        <RATIONALE>
        [Briefly explain your rationale for the generated prompt]
        </RATIONALE>"""
        
        user_prompt = f"Please generate a clear and expanded prompt based on the following input: {prompt}"
        return system_prompt, user_prompt

    def no_shot_prompting(self, prompt):
        system_prompt = """You are a helpful assistant that generates no-shot prompts. Your task is to take the user's input and generate a prompt that doesn't rely on examples or prior knowledge, focusing solely on the given task.
        
        Format your response using the following structure:
        
        <PROMPT>
        [Your generated no-shot prompt goes here]
        </PROMPT>
        
        <INSTRUCTIONS>
        [Provide clear, step-by-step instructions for completing the task]
        </INSTRUCTIONS>
        
        <OUTPUT_FORMAT>
        [Describe the expected format or structure of the answer]
        </OUTPUT_FORMAT>"""
        
        user_prompt = f"Generate a no-shot prompt based on the following input, ensuring it doesn't rely on examples or prior knowledge: {prompt}"
        return system_prompt, user_prompt

    def few_shot_prompting(self, prompt, num_examples=3):
        system_prompt = f"""You are a helpful assistant that generates few-shot prompts. Your task is to take the user's input and generate a prompt that includes {num_examples} relevant examples to guide the response.
        
        Format your response using the following structure:
        
        <PROMPT>
        [Restate the original prompt]
        </PROMPT>
        
        <EXAMPLES>
        [Provide {num_examples} concise, relevant examples related to the prompt]
        </EXAMPLES>
        
        <TASK>
        [Provide instructions on how to respond to the original prompt using insights from the examples]
        </TASK>"""
        
        user_prompt = f"Generate a few-shot prompt with {num_examples} relevant examples based on the following input: {prompt}"
        return system_prompt, user_prompt

    def include_exclude_prompting(self, prompt, include=None, exclude=None):
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
        return system_prompt, user_prompt
import json

def save_to_json(data, filename="output.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, separators=(',', ': '))

# Example usage
if __name__ == "__main__":
    generator = PromptGenerator()

    prompts_to_test = [
        {"technique": "general", "prompt": "Explain the importance of renewable energy"},
        {"technique": "no_shot", "prompt": "Describe the process of photosynthesis"},
        {"technique": "few_shot", "prompt": "Provide tips for effective time management"},
        {"technique": "include_exclude", "prompt": "Discuss the impact of social media", "include": ["mental health", "productivity"], "exclude": ["specific platforms", "technical details"]}
    ]

    results = []
    for test in prompts_to_test:
        result = generator.generate_prompt(test["prompt"], technique=test["technique"], **{k: v for k, v in test.items() if k not in ["technique", "prompt"]})
        results.append(result)

    save_to_json(results)
    print(f"Results have been saved to output.json")