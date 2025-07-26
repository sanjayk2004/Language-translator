import streamlit as st
from googletrans import Translator

translator = Translator()

st.title("English to Malayalam Translator (Google API)")

text = st.text_area("Enter English text:")

if st.button("Translate"):
    if text.strip():
        translated = translator.translate(text, src='en', dest='ml')
        st.success(translated.text)
    else:
        st.warning("Please enter some text.")
