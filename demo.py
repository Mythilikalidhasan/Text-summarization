
import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

st.set_page_config(
    page_title="Text Summarization",
    page_icon="🤖"
)

st.title("AI Text Summarization")
st.write("Convert long paragraphs into short and meaningful summaries using AI.")

@st.cache_resource
def load_model():
    model_name = "sshleifer/distilbart-cnn-12-6"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    return tokenizer, model

text = st.text_area(
    "Enter your text here:",
    height=250,
    placeholder="Paste your paragraph here..."
)

if st.button("Generate Summary"):
    if not text.strip():
        st.warning("Please enter your text!")

    else:
        try:
            with st.spinner("Generating summary..."):
                tokenizer, model = load_model()

                inputs = tokenizer(
                    text,
                    return_tensors="pt",
                    max_length=1024,
                    truncation=True
                )

                with torch.no_grad():
                    summary_ids = model.generate(
                        **inputs,
                        max_new_tokens=100,
                        num_beams=4,
                        do_sample=False
                    )

                summary = tokenizer.decode(
                    summary_ids[0],
                    skip_special_tokens=True
                )

            st.subheader("Summarized Text")
            st.success(summary)

        except Exception:
            st.error(
                "Unable to generate summary. "
                "Please check your internet connection and model availability."
            )
