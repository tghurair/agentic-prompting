import streamlit as st

class OverviewPage:
    def render(self):
        st.title("🗂 Overview Guide")
        st.write("""
        Welcome to the AI Prompt Engineering Assistant. This tool allows you to explore various prompt engineering techniques 
        and experiment with AI responses interactively.

        **Main Features:**
        
        - **Prompt Engineering Tab**: Create and refine prompts using different techniques like Few-Shot and Chain-of-Thought.
        - **Playground Tab**: Test your prompts in a sandbox environment with different AI models.
        - **Agentic Prompting Tab**: Optimize prompts and analyze them deeply using advanced agentic prompting techniques.
        
        Navigate through the tabs to explore each functionality in detail.
        """)
