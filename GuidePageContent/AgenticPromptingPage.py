import streamlit as st

class AgenticPromptingPage:
    def render(self):
        st.title("🤖 Agentic Prompting Guide")

        st.markdown("Welcome to the Agentic Prompting tab, where advanced AI-powered prompt optimization takes place.")

        st.markdown("---")

        st.subheader("How It Works")
        st.markdown("This feature leverages a sophisticated AI agent to enhance your prompts through a two-step process:")

        st.info("##### **1. Deep Analysis**")
        st.markdown("""
        The AI agent thoroughly analyzes your prompt idea by:
        - Examining the context and intent of your input
        - Assessing the complexity of the task
        - Identifying key elements and requirements
        - Determining the most suitable prompt engineering technique
        """)

        st.success("##### **2. Intelligent Generation**")
        st.markdown("""
        Based on the analysis, the agent crafts an optimized prompt by:
        - Applying the chosen prompt engineering technique
        - Restructuring and refining the original input
        - Enhancing clarity and specificity
        - Ensuring alignment with the intended goal
        - Providing a detailed explanation of the optimization process
        """)

        st.markdown("---")

        st.subheader("How to Use")
        st.markdown("Follow these steps to make the most of this powerful feature:")
        steps = [
            "Enter your prompt idea in the text area. Be as detailed and specific as possible.",
            "Click 'Generate Agentic Prompt' to initiate the optimization process.",
            "The system will analyze and enhance your prompt behind the scenes.",
            "Review the results: Generated Prompt and Analysis."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"{i}. {step}")

        st.markdown("---")

        st.subheader("Tips for Best Results")
        st.markdown("""
        - Provide clear context in your initial prompt
        - Be specific about your desired outcome
        - Experiment with different phrasings
        - Review the analysis to understand the AI's reasoning
        """)

        st.markdown("---")

        st.subheader("Why Use Agentic Prompting?")
        st.markdown("""
        This advanced approach allows you to leverage AI power to create more effective, nuanced, and context-aware prompts. 
        It's particularly useful for:
        - Complex tasks
        - Fine-tuning prompts for optimal results
        - Understanding AI reasoning processes
        """)

        st.markdown("---")

        st.subheader("Example Use Cases")
        st.markdown("""
        1. **Content Creation**: Optimize prompts for generating creative writing ideas
        2. **Data Analysis**: Refine prompts for extracting insights from complex datasets
        3. **Problem Solving**: Enhance prompts for breaking down and solving multi-step problems
        4. **Language Translation**: Improve prompts for nuanced and context-aware translations
        """)

        st.markdown("---")

        st.info("Experiment with different prompt ideas and see how the Agentic Prompting system can elevate your AI interactions!")
