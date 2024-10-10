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
from GuidePageContent.OverviewPage import OverviewPage
from GuidePageContent.PromptEngineeringPage import PromptEngineeringPage
from GuidePageContent.AgenticPromptingPage import AgenticPromptingPage
from GuidePageContent.PlaygroundPage import PlaygroundPage

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
        ["General Prompting", "No-Shot Prompting", "Few-Shot Prompting", 
         "Include-Exclude Prompting", "Chain of Thought", "Chain of Thought with Reflection", "ReAct Prompting"]
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

def guide_page():
    st.title("AI Prompt Engineering Assistant Guide")
    
    tabs = st.tabs(["Overview", "Agentic Prompting", "Prompt Engineering", "Playground"])
    
    with tabs[0]:
        OverviewPage().render()
    
    with tabs[1]:
        AgenticPromptingPage().render()
    
    with tabs[2]:
        PromptEngineeringPage().render()
    
    with tabs[3]:
        PlaygroundPage().render()

def main_interface():
    st.title("AI Prompt Engineering Assistant")
    
    tabs = st.tabs(["Agentic Prompting", "Prompt Engineering", "Playground"])
    
    with tabs[0]:
        agentic_prompting_tab(st.session_state.openai_client)
    
    with tabs[1]:
        prompt_engineering_tab(st.session_state.openai_client)
    
    with tabs[2]:
        playground_tab(st.session_state.openai_client)

def main():
    st.set_page_config(layout="wide")
    
    # Navigation buttons
    page = st.sidebar.radio("Go to", ["Guide", "Prompt Crafting Studio"])
    
    if page == "Guide":
        guide_page()
    else:
        # Only show API key input and main interface if Prompt Crafting Studio is selected
        api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
        
        if api_key:
            st.session_state.openai_client = get_openai_client(api_key)
            main_interface()
        else:
            st.warning("Please enter your OpenAI API key in the sidebar to access the Prompt Crafting Studio.")

if __name__ == "__main__":
    main()