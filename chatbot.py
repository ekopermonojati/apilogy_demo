import streamlit as st
import numpy as np 
import random
import time
import requests

st.title("Apilogy Bot Example")
st.sidebar.text("Model : Telkom LLM Ver. 0.0.3")
st.sidebar.link_button("Go to API page", "https://www.apilogy.id/api/detail/telkom_ai_dag/name/Telkom-LLM/version/0.0.3")
apilogy_key = st.sidebar.text_input("Apilogy API Key", type="password")
bot_system = st.sidebar.text_area("System Message",value="You are a nice chatbot having a conversation with a human")
temperature = st.sidebar.number_input(label="Temperature", min_value=0, max_value=1, value=0)
max_gen_len = st.sidebar.number_input(label="Max Tokens", min_value=50, max_value=500, value=100)
button = st.sidebar.button(label="Set and start New Chat")


api_key = apilogy_key 
url = "https://telkom-ai-dag.api.apilogy.id/Telkom-LLM/0.0.3/chat/completion/telkomai"
headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-api-key': api_key
        }
# Initialize chat history
if "messages" not in st.session_state or button:
    st.session_state.messages = [{'role': 'system', 'content': bot_system}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["content"] and message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# Streamed response 
def assistant_response_generator(data_res):
    # construct message chain
    st.session_state.messages.append({"role": "user", "content": data_res})
    #construct payload
    jsons = {
                'message': st.session_state.messages,
                'temperature': temperature,
                'max_gen_len': max_gen_len
            }
    response = requests.post(url, headers=headers, json=jsons)
    data = response.json()
    print(jsons)
    print(data)
    if response.status_code == 200 and 'result' in data:
        data_res = data['result']
        for word in data_res.split():
            yield word + " "
            time.sleep(0.05)
    elif response.status_code == 401 :
        yield "Unauthorized access. Please check your api key"
    else:
        yield "Error : " + str(response.status_code)
    

if "mulai" not in st.session_state:
    with st.chat_message("assistant"):
        st.write_stream(response_generator())
        st.session_state.mulai = 1

prompt = st.chat_input("Enter user message...")
if prompt:
    with st.chat_message("user"):
        st.write(f"{prompt}")
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("..."):
            response = st.write_stream(assistant_response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})