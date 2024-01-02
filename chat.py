import os
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="Converational Chatbot")

st.header("Hi, Chat with me!")

from dotenv import load_dotenv
load_dotenv()

chat = ChatOpenAI(temperature=0.5)

if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content="Hi, I am a chatbot. You can ask me anything!")
    ]

def get_openai_response(query):
    st.session_state['flowmessages'].append(HumanMessage(content=query))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))

    return answer.content

input = st.text_input("Input: ", key="input")
response = get_openai_response(input)

submit = st.button("Submit")

if submit:
    st.write(response)
