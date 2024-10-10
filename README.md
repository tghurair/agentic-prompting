# Agentic Prompting: AI Prompt Engineering Assistant

A comprehensive tool designed to help you explore and master various prompt engineering techniques. This project leverages LLMs (Large Language Models) to optimize and enhance your prompt crafting skills, making it easier to generate effective and context-aware prompts for a wide range of applications.

## Table of Contents
1. [Features](#features)
2. [How to Use](#how-to-use)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Tools Used](#tools-used)
6. [Contributing](#contributing)

## Features
### 1. Agentic Prompting
The Agentic Prompting feature is a sophisticated tool that enhances your prompts through a two-step process:

#### 1. Deep Analysis
The AI agent thoroughly analyzes your prompt idea by:
- Examining the context and intent of your input
- Assessing the complexity of the task
- Identifying key elements and requirements
- Determining the most suitable prompt engineering technique

#### 2. Intelligent Generation
Based on the analysis, the agent crafts an optimized prompt by:
- Applying the chosen prompt engineering technique
- Restructuring and refining the original input
- Enhancing clarity and specificity
- Ensuring alignment with the intended goal
- Providing a detailed explanation of the optimization process

We utilized CrewAI for agent implementation and orchestration, which was instrumental in the Agentic Prompting feature.

### 2. Prompt Engineering Techniques
Explore a variety of prompt engineering techniques, including:
- **General Prompting**: Suitable for open-ended questions and creative tasks.
- **Zero-Shot Prompting**: Ideal for straightforward tasks without examples.
- **Few-Shot Prompting**: Provides examples to guide the model for complex tasks.
- **Include-Exclude Prompting**: Specifies elements to include or exclude in responses.
- **Chain of Thought (CoT)**: Breaks down complex problems into sequential reasoning steps.
- **Chain of Thought Reflection**: Incorporates a reflection step for self-correction.
- **ReAct Prompting**: Combines reasoning and action steps for dynamic interactions.

### 3. Playground
The Playground tab allows you to experiment with different prompts and see how AI models respond in real-time. It provides a sandbox environment to test and refine your prompts, enhancing your understanding of AI behavior and response patterns.

## How to Use

1. **Start with the Prompt Engineering Tab**: Learn about different techniques and practice crafting prompts.
2. **Experiment in the Playground**: Test your prompts with various AI models and refine your skills.
3. **Leverage Agentic Prompting**: Use this feature for advanced optimization of your prompts.
4. **Iterate and Refine**: Continuously improve your prompt crafting skills across all tabs.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-repo/agentic-prompting.git
cd agentic-prompting
pip install -r requirements.txt
```

## Usage

Run the application using locally using Streamlit:

streamlit run app.py

## Tools Used
- Streamlit
- CrewAI
- OpenAI

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests. 
