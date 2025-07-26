import streamlit as st
import requests

st.title("English to Malayalam Translator (LibreTranslate)")

text = st.text_area("Enter English text:")

if st.button("Translate"):
    if text.strip():
        payload = {
            'q': text,
            'source': 'en',
            'target': 'ml',
            'format': 'text'
        }
        response = requests.post("https://libretranslate.de/translate", data=payload)
        result = response.json()
        st.success(result['translatedText'])
    else:
        st.warning("Please enter some text.")
