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
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # You can swap this to another API like: https://translate.argosopentech.com
        api_url = "https://libretranslate.de/translate"

        response = requests.post(api_url, data=payload, headers=headers)

        st.text(f"Status Code: {response.status_code}")  # For debug
        st.text(f"Response Text: {response.text}")       # For debug

        if response.status_code == 200:
            result = response.json()
            st.success(result['translatedText'])
        else:
            st.error("Translation failed. Please try again later.")
    else:
        st.warning("Please enter some text.")
