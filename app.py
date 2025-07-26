import streamlit as st
import requests

st.title("English to Malayalam Translator")

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

        # Use actual translation API endpoint
        api_url = "https://translate.argosopentech.com/translate"

        response = requests.post(api_url, data=payload, headers=headers)

        if response.status_code == 200:
            try:
                result = response.json()
                st.success(result['translatedText'])
            except Exception:
                st.error("Error parsing translation response.")
        else:
            st.error(f"Translation failed. Status: {response.status_code}")
    else:
        st.warning("Please enter some text.")
