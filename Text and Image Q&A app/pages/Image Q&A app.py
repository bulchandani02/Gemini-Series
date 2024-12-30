from dotenv import load_dotenv
load_dotenv()   ## loading all the environment variables


import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 

## Function to load Gemini Pro model and get response

model=genai.GenerativeModel("gemini-1.5-flash")   ## Gemini-pro is text generation model

def response_gemini(question,image):
    if question!="":
        response=model.generate_content([question,image])
    else:
        response=model.generate_content(image)
    return response.text


## Initiliazing streamlit UI

st.set_page_config(page_title="Q&A App")

st.header("Gemini 1.5 flash - Q&A LLM application")

input=st.text_input("Input: ",key="input")

upload_file=st.file_uploader("Choose an image: ", type=["jpg","jpeg","png"])
image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image, caption="Uploaded image", use_column_width=True)


submit=st.button("Tell me about image")


## When submit is selected
if submit:
    response=response_gemini(input,image)
    st.subheader("Gemini Response")
    st.write(response)

