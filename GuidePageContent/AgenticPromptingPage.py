import streamlit as st

class AgenticPromptingPage:
    def render(self):
        st.title("🤖 Agentic Prompting Guide")
        st.write("""
        The Agentic Prompting tab offers advanced prompt optimization. Here's how to utilize this feature:

        1. **Enter your prompt idea** in the text area, providing as much detail as possible.
        2. **Click 'Generate Agentic Prompt'** to initiate the process.
        3. The system will **analyze your prompt**, optimize it, and provide an in-depth analysis of its reasoning.
        4. The generated prompt and analysis will be displayed below for your review.
        
        This guide helps you understand the workflow for agentic prompting and how to leverage its analytical capabilities.
        """)
