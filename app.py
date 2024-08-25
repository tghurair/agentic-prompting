#TODO Build Streamlit App
import streamlit as st
from models.prompt_generator import generate_prompt

def main():
    st.title("AI Prompt Engineering Assistant")
    user_input = st.text_area("Enter your prompt idea:")
    techniques = st.multiselect(
        "Select prompt engineering techniques:",
        ["Chain of Thought", "Few-Shot Prompting", "Tree of Thought"]
    )
    if st.button("Generate Enhanced Prompt"):
        if user_input and techniques:
            enhanced_prompt = generate_prompt(user_input, techniques)
            st.subheader("Enhanced Prompt:")
            st.write(enhanced_prompt)
        else:
            st.warning("Please enter a prompt idea and select at least one technique.")

if __name__ == "__main__":
    main()