import streamlit as st
from techniques.few_shot_prompt import FewShotPrompt
from techniques.general_prompt import GeneralPrompt
from techniques.include_exclude_prompt import IncludeExcludePrompt
from openai import OpenAI
from techniques.chain_of_thought import ChainOfThoughtPrompt
from techniques.cot_reflection import ChainOfThoughtReflection
from techniques.no_shot_prompt import NoShotPrompt
from techniques.Agentic_prompting import AgenticPrompting
from techniques.ReAct import ReActPrompt

# Add this at the beginning of the script
if 'current_tab' not in st.session_state:
    st.session_state.current_tab = "Prompt Engineering"

# Initialize session state
if 'openai_client' not in st.session_state:
    st.session_state.openai_client = None

@st.cache_resource
def get_openai_client(api_key):
    return OpenAI(api_key=api_key)

def get_prompt_technique(technique_name, client):
    techniques = {
        "General Prompting": GeneralPrompt,
        "Few-Shot Prompting": FewShotPrompt,
        "Include-Exclude Prompting": IncludeExcludePrompt,
        "Chain of Thought": ChainOfThoughtPrompt,
        "Chain of Thought with Reflection": ChainOfThoughtReflection,
        "No-Shot Prompting": NoShotPrompt,
        "ReAct Prompting": ReActPrompt
    }
    return techniques[technique_name](client)

def generate_prompt(technique, user_input, **kwargs):
    return technique.generate(user_input, **kwargs)

def prompt_engineering_tab(client):
    st.title("AI Prompt Engineering Assistant")
    
    user_input = st.text_area("Enter your prompt idea:", key="prompt_engineering_input")
    
    technique = st.radio(
        "Select a prompt engineering technique:",
        ["General Prompting", "Few-Shot Prompting", "Include-Exclude Prompting", 
         "Chain of Thought", "Chain of Thought with Reflection", "No-Shot Prompting", "ReAct Prompting"]
    )
    
    prompt_technique = get_prompt_technique(technique, client)
    
    kwargs = {}
    if technique == "Few-Shot Prompting":
        kwargs['num_examples'] = st.number_input("Number of examples:", min_value=1, max_value=15, value=1, step=1)
    elif technique == "Include-Exclude Prompting":
        col1, col2 = st.columns(2)
        with col1:
            kwargs['include'] = st.text_area("Include in prompt:", key="include_prompt")
        with col2:
            kwargs['exclude'] = st.text_area("Exclude from prompt:", key="exclude_prompt")
    elif technique == "ReAct Prompting":
        kwargs['tool'] = st.text_input("Specify a tool (optional):", key="react_tool")

    if st.button("Generate Prompt"):
        if user_input:
            with st.spinner("Generating prompt..."):
                generated_prompt = generate_prompt(prompt_technique, user_input, **kwargs)
                st.subheader("Generated Prompt:")
                st.code(generated_prompt, language="markdown")
        else:
            st.warning("Please enter a prompt idea and provide necessary information for the selected technique.")

def generate_ai_response(client, model, system_prompt, user_input):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

def playground_tab(client):
    st.title("Prompt Playground")
    
    model = st.selectbox("Select Model", ["gpt-4o-mini", "gpt-4o", "o1-preview"])
    system_prompt = st.text_area("System Prompt:", "You are a helpful assistant.", key="system_prompt")
    user_input = st.text_area("User Input:", key="playground_input")
    
    if st.button("Generate Response"):
        if user_input:
            with st.spinner("Generating response..."):
                ai_response = generate_ai_response(client, model, system_prompt, user_input)
                st.subheader("AI Response:")
                st.write(ai_response)
        else:
            st.warning("Please enter a user input.")

def get_agentic_prompt(client):
    return AgenticPrompting(client)

def generate_agentic_prompt(agentic_prompt, user_input):
    return agentic_prompt.generate(user_input)

def agentic_prompting_tab(client):
    st.title("Agentic Prompting")
    
    agentic_prompt = AgenticPrompting(client)
    
    with st.form(key='agentic_form'):
        user_input = st.text_area("Enter your prompt idea:", key="agentic_input")
        submit_button = st.form_submit_button("Generate Agentic Prompt")

    if submit_button:
        if user_input:
            with st.spinner("Generating Agentic Prompt..."):
                try:
                    result = agentic_prompt.generate(user_input)
                    st.subheader("Generated Prompt:")
                    st.code(result["prompt"], language="markdown")
                    st.subheader("Analysis:")
                    st.write(result["analysis"])
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a prompt idea.")

def how_to_use_tab():
    st.title("How to Use the AI Prompt Engineering Assistant")
    
    st.header("Getting Started")
    st.write("1. Enter your OpenAI API key in the sidebar.")
    st.write("2. Navigate to the 'Prompt Engineering' tab.")
    
    st.header("Using the Prompt Engineering Assistant")
    st.write("1. Enter your prompt idea in the text area.")
    st.write("2. Select a prompt engineering technique.")
    st.write("3. Provide additional information if required by the selected technique.")
    st.write("4. Click the 'Generate Prompt' button to see the result.")
    
    st.header("Prompt Engineering Techniques")
    st.subheader("1. General Prompting")
    st.write("This technique generates a prompt based on your input without any additional constraints.")
    
    st.subheader("2. Few-Shot Prompting")
    st.write("This technique uses examples to guide the AI in generating a more specific prompt. Provide one example per line in the text area.")
    
    st.subheader("3. Include-Exclude Prompting")
    st.write("This technique allows you to specify elements to include or exclude from the generated prompt. Use the provided text areas to enter your preferences.")

    st.header("Using the Playground")
    st.write("1. Navigate to the 'Playground' tab.")
    st.write("2. Select a model from the dropdown menu.")
    st.write("3. Optionally, modify the system prompt.")
    st.write("4. Enter your user input (you can paste the generated prompt from the Prompt Engineering tab).")
    st.write("5. Click the 'Generate Response' button to see the AI's response.")

    st.header("Using Agentic Prompting")
    st.write("1. Navigate to the 'Agentic Prompting' tab.")
    st.write("2. Enter your prompt idea in the text area.")
    st.write("3. Click the 'Generate Agentic Prompt' button.")
    st.write("4. The system will analyze your prompt and generate an optimized version using AI agents.")

def main():
    st.set_page_config(layout="wide")
    st.sidebar.title("Settings")
    
    # API key input in sidebar
    api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
    
    if api_key:
        st.session_state.openai_client = get_openai_client(api_key)
    
    if not st.session_state.openai_client:
        st.warning("Please enter your OpenAI API key in the sidebar.")
        return

    # Tab selection
    tab1, tab2, tab3, tab4 = st.tabs(["Prompt Engineering", "Playground", "Agentic Prompting", "How to Use"])
    
    with tab1:
        prompt_engineering_tab(st.session_state.openai_client)
    
    with tab2:
        playground_tab(st.session_state.openai_client)
    
    with tab3:
        agentic_prompting_tab(st.session_state.openai_client)
    
    with tab4:
        how_to_use_tab()

if __name__ == "__main__":
    main()