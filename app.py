import streamlit as st
import requests

API_URL = "https://translate.argosopentech.com/translate"

def translate(text, source="en", target="ml"):
    payload = {
        "q": text,
        "source": source,
        "target": target,
        "format": "text"
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        if response.status_code == 200:
            return response.json()["translatedText"]
        else:
            return f"Translation failed: {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

st.title("English to Malayalam Translator 🗣️🌐")
user_input = st.text_area("Enter English Text", height=150)

if st.button("Translate"):
    if user_input.strip():
        translation = translate(user_input.strip())
        st.success(translation)
    else:
        st.warning("⚠️ Please enter some text.")
