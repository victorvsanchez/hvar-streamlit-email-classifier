import streamlit as st
import openai

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("📧 Copel Email Classifier") 

uploaded_file = st.file_uploader("Faça upload de um anexo", type=("txt", "md")) 

question = st.text_input(
    "Escreva abaixo o corpo do e-mail",
    disabled=not uploaded_file,
)

if uploaded_file and question and not openai_api_key:
    st.info("Adicione sua key do Open AI para continuar:")

if uploaded_file and question and openai_api_key:
    #article = uploaded_file.read().decode()
    #prompt = f"""{anthropic.HUMAN_PROMPT} Here's an article:\n\n
    #{article}\n\n\n\n{question}{anthropic.AI_PROMPT}"""

    #client = anthropic.Client(api_key=openai_api_key)
    #response = client.completions.create(
        #prompt=prompt,
        #stop_sequences=[anthropic.HUMAN_PROMPT],
        #model="claude-v1", #"claude-2" for Claude 2 model
        #max_tokens_to_sample=100,
    #)
    st.write("### Answer")
    #st.write(response.completion)