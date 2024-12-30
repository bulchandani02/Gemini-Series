from dotenv import load_dotenv
load_dotenv()   ## loading all the environment variables


import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 

## Function to load Gemini Pro model and get response

model=genai.GenerativeModel("gemini-pro")   ## Gemini-pro is text generation model

chat=model.start_chat(history=[])

def response_gemini(question):
    response=chat.send_message(question, stream=True)
    return response


## Initiliazing streamlit UI

st.set_page_config(page_title="Q&A App")

st.header("Gemini Pro - Q&A LLM application")

## Initialize session state for the chat history if it doesn't exist 
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")


## When submit is selected
if submit and input:
    response=response_gemini(input)
    ## Add user query and response to session chat history
    st.session_state['chat_history'].append(("User",input))

    ## Displying the response
    st.subheader("Gemini Response")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("BOT",chunk.text))

## Displying the history
st.subheader("Chat history")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
    

