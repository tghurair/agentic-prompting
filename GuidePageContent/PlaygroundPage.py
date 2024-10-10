import streamlit as st

class PlaygroundPage:
    def render(self):
        st.title("🎮 Playground Guide")

        st.markdown("Welcome to the Playground tab, where you can experiment with different prompts and see how AI models respond in real-time.")

        st.markdown("---")

        st.subheader("What are System and User Prompts?")
        st.markdown("""
        In the context of AI interactions, we often use two types of prompts:

        1. **System Prompt**: Sets the overall context and behavior for the AI assistant.
        2. **User Prompt**: The specific query or instruction given to the AI within the established context.
        """)

        st.markdown("---")

        st.subheader("How to Use the Playground")
        st.markdown("Follow these steps to make the most of this feature:")
        steps = [
            "Select an AI model from the dropdown menu.",
            "Craft a system prompt to set the context for your AI assistant.",
            "Enter your user message in the provided text area.",
            "Click 'Generate Response' to see the AI's reply.",
            "Experiment with different combinations of system and user prompts."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"{i}. {step}")

        st.markdown("---")

        st.subheader("Understanding System Prompts")
        st.info("##### **System Prompt**")
        st.markdown("""
        A system prompt is used to:
        - Define the AI's role and personality
        - Set boundaries for the conversation
        - Provide background information or context
        - Specify output formats or requirements

        Example: "You are a helpful assistant with expertise in climate science. Provide concise, fact-based responses."
        """)

        st.markdown("---")

        st.subheader("Crafting Effective User Prompts")
        st.success("##### **User Prompt**")
        st.markdown("""
        User prompts are the specific questions or instructions you give to the AI. To create effective user prompts:
        - Be clear and specific in your request
        - Provide necessary context
        - Break complex queries into smaller parts
        - Use the appropriate prompt engineering technique for your task

        Example: "Explain the greenhouse effect and its impact on global temperatures in simple terms."
        """)

        st.markdown("---")

        st.subheader("Tips for Effective Playground Use")
        st.markdown("""
        - Experiment with different system prompts to see how they affect the AI's behavior
        - Try various prompt engineering techniques in your user prompts
        - Pay attention to how small changes in wording can lead to different responses
        - Use the playground to refine your prompts before using them in real-world applications
        - Compare responses from different AI models to understand their strengths and limitations
        """)

        st.markdown("---")

        st.info("Experiment with different combinations of system and user prompts to see how they influence the AI's responses and improve your prompt engineering skills!")
