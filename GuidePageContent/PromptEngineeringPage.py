import streamlit as st

class PromptEngineeringPage:
    def render(self):
        st.title("🧙‍♂️ Prompt Engineering Guide")

        st.markdown("Welcome to the Prompt Engineering tab, where you can explore and master various prompt engineering techniques.")

        st.markdown("---")

        st.subheader("What is Prompt Engineering?")
        st.markdown("""
        Prompt engineering is the art and science of crafting effective prompts to guide AI models in generating desired outputs. 
        It involves designing, refining, and optimizing input prompts to improve the quality, relevance, and accuracy of AI-generated responses.
        """)

        st.markdown("---")

        st.subheader("How to Use")
        st.markdown("Follow these steps to make the most of this feature:")
        steps = [
            "Enter your initial prompt idea in the provided text area.",
            "Select your preferred prompt engineering technique from the available options.",
            "Provide any additional input if required by the chosen technique.",
            "Click 'Generate Prompt' to see the results of your input.",
            "Review the generated prompt and use it with your preferred AI model."
        ]
        for i, step in enumerate(steps, 1):
            st.markdown(f"{i}. {step}")

        st.markdown("---")

        st.subheader("Prompt Engineering Techniques")
        techniques = [
            {
                "name": "General Prompting",
                "description": "A basic technique for generating prompts without additional constraints, suitable for a wide range of tasks.",
                "use_case": "Ideal for open-ended questions, creative tasks, or when you want the AI to have maximum flexibility in its response.",
                "example": "Explain the concept of climate change and its potential impacts on global ecosystems."
            },
            {
                "name": "Zero-Shot Prompting",
                "description": "Generates prompts for tasks where the model can directly produce an answer without examples or specific training.",
                "use_case": "Suitable for straightforward tasks, short answers, and classification when the model already has the necessary knowledge.",
                "example": "Classify the following sentence as positive, negative, or neutral: 'The new policy has sparked heated debates among experts.'"
            },
            {
                "name": "Few-Shot Prompting",
                "description": "Uses a small number of examples (usually depending on the task complexity) to guide the AI in generating more specific and contextually appropriate responses. This technique can also facilitate in-context learning by including demonstrations in the prompt to enhance the model's performance.",
                "use_case": "Ideal for complex tasks and for guiding the model to understand the expected output by providing relevant examples.",
                "example": "Translate English to French:\nEnglish: The weather is nice today.\nFrench: Le temps est beau aujourd'hui.\nEnglish: I love learning new languages.\nFrench: J'adore apprendre de nouvelles langues.\nEnglish: What time is the meeting?\nFrench:"
            },
           {
                "name": "Include-Exclude Prompting",
                "description": "A prompting strategy that explicitly defines elements to include or exclude in the model's response or during the reasoning process. It guides the model to focus on specified topics or avoid particular subjects, enhancing control over generated outputs.",
                "use_case": "Ideal for scenarios where precise control over content is required, such as ensuring certain details are highlighted or specific topics are omitted from the response.",
                "example": "Write a short story about a future society. Include: advanced AI, sustainable energy. Exclude: dystopian themes, space travel."
            },
            {
                "name": "Chain of Thought (CoT)",
                "description": "Breaks down complex problems into sequential reasoning steps, helping the model articulate its thought process before arriving at the final answer. This method improves accuracy and interpretability in multi-step tasks.",
                "use_case": "Effective for tasks that require logical progression, such as solving math problems, logical reasoning, or handling ambiguous scenarios.",
                "example": "Solve this problem step-by-step: If a train travels 120 km in 2 hours, and then an additional 180 km in 3 hours, what is the average speed for the entire journey?"
            },
            {
                "name": "Chain of Thought Reflection",
                "description": "Extends Chain of Thought (CoT) by incorporating a reflection step, where the model re-evaluates its previous reasoning to identify errors and consider potential improvements. This iterative self-correction helps refine the output and improve complex problem-solving capabilities.",
                "use_case": "Ideal for tasks that benefit from self-correction, such as detailed planning, hypothesis generation, or scenarios where initial solutions may need revision based on new information or insights.",
                "example": "Develop a plan to reduce a company's carbon footprint. After outlining the plan, reflect on potential challenges and weaknesses. Suggest refinements, then present a revised, more robust plan based on the reflections."
            },
            {
                "name": "ReAct Prompting",
                "description": "Combines reasoning and action steps, allowing the model to dynamically switch between thought processes and external actions, such as performing searches or querying APIs.",
                "use_case": "Ideal for scenarios where the model needs to interact with external tools or databases, such as web search APIs, to provide more reliable, updated information and handle complex queries that require external validation or data retrieval.",
                "example": "You are a customer support assistant. First, understand the customer's request and then use the provided API to check the product availability. If the product is available, provide purchase options; otherwise, suggest similar alternatives."
            }
        ]

        for technique in techniques:
            st.info(f"##### **{technique['name']}**")
            st.markdown(f"**Description:** {technique['description']}")
            st.markdown(f"**Use Case:** {technique['use_case']}")
            st.markdown(f"**Example:** {technique['example']}")
            st.markdown("---")

        st.subheader("Tips for Effective Prompt Engineering")
        st.markdown("""
        - Be clear and specific in your instructions
        - Provide context when necessary
        - Experiment with different techniques for the same task
        - Iterate and refine your prompts based on the results
        - Consider the strengths and limitations of the AI model you're using
        """)

        st.markdown("---")

        st.info("Experiment with different prompt engineering techniques to enhance your AI interactions and achieve better results!")
