import streamlit as st

class PromptEngineeringPage:
    def render(self):
        st.title("🧙‍♂️ Prompt Engineering Guide")
        st.write("""
        The Prompt Engineering tab is where you'll create and refine your prompts. Here's how to use it effectively:

        1. **Enter your initial prompt idea** in the provided text area.
        2. **Select your preferred prompt engineering technique** from the available options.
        3. Some techniques may require additional input. Follow the on-screen instructions if prompted.
        4. When ready, click **'Generate Prompt'** to see the results of your input.

        ### Prompt Engineering Techniques Overview:
        - **General Prompting**: Basic technique for generating prompts without additional constraints.
        - **Few-Shot Prompting**: Use examples to guide the AI in generating more specific prompts.
        - **Include-Exclude Prompting**: Customize prompts by specifying what should be included or excluded.
        - **Chain of Thought**: Break down complex problems into steps for better clarity.
        - **ReAct Prompting**: Combines reasoning and action, suitable for analytical and task-oriented prompts.
        
        Use these techniques to experiment and improve your prompt engineering skills.
        """)
