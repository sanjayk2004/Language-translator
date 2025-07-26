import streamlit as st
from deep_translator import GoogleTranslator

st.title("English to Malayalam Translator")

user_input = st.text_area("Enter English Text")

if st.button("Translate"):
    if user_input.strip():
        try:
            translated_text = GoogleTranslator(source='en', target='ml').translate(user_input)
            st.success(translated_text)
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text.")

