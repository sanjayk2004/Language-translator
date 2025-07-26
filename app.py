import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Load model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-ml"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Translation function
def translate(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

# Streamlit UI
st.title("English to Malayalam Translator")
user_input = st.text_area("Enter English Text")

if st.button("Translate"):
    if user_input.strip():
        translation = translate(user_input)
        st.success(translation)
    else:
        st.warning("Please enter some text.")
