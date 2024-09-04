import streamlit as st
from techniques.prompt_techniques.few_shot_prompt import FewShotPrompt
from techniques.prompt_techniques.general_prompt import GeneralPrompt
from techniques.prompt_techniques.include_exclude_prompt import IncludeExcludePrompt

def main():
    st.title("AI Prompt Engineering Assistant")
    
    user_input = st.text_area("Enter your prompt idea:")
    
    techniques = st.multiselect(
        "Select prompt engineering techniques:",
        ["General Prompting", "Few-Shot Prompting", "Include-Exclude Prompting"]
    )
    
    generated_prompts = []

    for technique in techniques:
        if technique == "General Prompting":
            general_prompt = GeneralPrompt(user_input)
            generated_prompts.append(general_prompt.generate())

        elif technique == "Few-Shot Prompting":
            examples = st.text_area("Enter few-shot examples (one per line):", key="few_shot")
            if examples:
                few_shot_prompt = FewShotPrompt(user_input, examples.split('\n'))
                generated_prompts.append(few_shot_prompt.generate())

        elif technique == "Include-Exclude Prompting":
            col1, col2 = st.columns(2)
            with col1:
                include = st.text_area("Include in prompt:", key="include")
            with col2:
                exclude = st.text_area("Exclude from prompt:", key="exclude")
            if include or exclude:
                include_exclude_prompt = IncludeExcludePrompt(user_input, include, exclude)
                generated_prompts.append(include_exclude_prompt.generate())

    if st.button("Generate Prompt"):
        if user_input and generated_prompts:
            st.subheader("Generated Prompts:")
            for i, prompt in enumerate(generated_prompts, 1):
                st.write(f"{i}. {prompt}")
        else:
            st.warning("Please enter a prompt idea and select at least one technique.")

if __name__ == "__main__":
    main()