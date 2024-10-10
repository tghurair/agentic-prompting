import streamlit as st

class PlaygroundPage:
    def render(self):
        st.title("🎮 Playground Guide")
        st.write("""
        The Playground tab allows you to test your prompts and interact with the AI. Here's how to use it:

        1. **Select an AI model** from the dropdown menu to choose the language model for generating responses.
        2. **Craft a system prompt** to set the context for your AI assistant (e.g., "You are a helpful assistant.").
        3. **Input your user message** and then click 'Generate Response' to see the AI's reply.
        4. Experiment with different prompts to understand how each change affects the response.

        The Playground helps you gain insights into how AI responds to various inputs and contexts.
        """)
