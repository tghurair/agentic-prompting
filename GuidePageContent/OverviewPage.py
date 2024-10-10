import streamlit as st

class OverviewPage:
    def render(self):
        st.title("🗂 AI Prompt Engineering Assistant Overview")

        st.markdown("Welcome to the AI Prompt Engineering Assistant, your comprehensive tool for exploring and mastering various prompt engineering techniques.")

        st.markdown("---")

        st.subheader("What is Prompt Engineering?")
        st.markdown("""
        Prompt engineering is the art and science of crafting effective prompts to guide AI models in generating desired outputs. 
        It involves designing, refining, and optimizing input prompts to improve the quality, relevance, and accuracy of AI-generated responses.
        """)

        st.markdown("---")

        st.subheader("Main Features")
        st.warning("##### **1. Agentic Prompting Tab**")
        st.markdown("""
        Leverage advanced AI-powered prompt optimization:
        - Deep analysis of your prompt ideas
        - Intelligent generation of optimized prompts
        - Detailed explanations of the optimization process
        - Suggestions for improvement and refinement
        """)
        
        
        st.info("##### **2. Prompt Engineering Tab**")
        st.markdown("""
        Explore and master various prompt engineering techniques:
        - General Prompting
        - Zero-Shot Prompting
        - Few-Shot Prompting
        - Include-Exclude Prompting
        - Chain of Thought (CoT)
        - Chain of Thought Reflection
        - ReAct Prompting
        """)

        st.success("##### **3. Playground Tab**")
        st.markdown("""
        Test your prompts in a sandbox environment:
        - Experiment with different AI models
        - Craft system and user prompts
        - Analyze AI responses in real-time
        - Refine your prompting skills through practice
        """)

        st.markdown("---")

        st.subheader("How to Use This Tool")
        st.markdown("""
        1. Start with the Prompt Engineering tab to learn about different techniques
        2. Practice crafting prompts in the Playground tab
        3. Use the Agentic Prompting tab for advanced optimization of your prompts
        4. Iterate and refine your skills across all tabs
        """)

        st.markdown("---")

        st.subheader("Benefits of Prompt Engineering")
        st.markdown("""
        - Improve the quality and relevance of AI-generated responses
        - Enhance control over AI outputs
        - Solve complex problems more effectively
        - Optimize AI performance for specific tasks
        - Gain deeper insights into AI reasoning processes
        """)

        st.markdown("---")

        st.info("Navigate through the tabs to explore each functionality in detail and enhance your prompt engineering skills!")
