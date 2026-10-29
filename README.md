#  AI Text Summarization

A Streamlit web app that turns long paragraphs into short, meaningful summaries using a pre-trained transformer model.

##  About

Paste any long text (article, notes, report) and get a concise summary in seconds. The app uses **DistilBART**, a distilled version of BART fine-tuned on the CNN/DailyMail dataset, so it's fast while still producing good abstractive summaries.

##  Features

- Clean, simple Streamlit interface
- Abstractive summarization (rewrites, not just extracts sentences)
- Model cached with `st.cache_resource`, so it loads only once
- Input validation and error handling
- Runs fully locally, with no API key needed

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| UI | Streamlit |
| Model | `sshleifer/distilbart-cnn-12-6` (Hugging Face) |
| Libraries | Transformers, PyTorch |

##  How It Works

1. User pastes text into the text area
2. Text is tokenized (truncated to 1024 tokens)
3. DistilBART generates a summary using beam search (`num_beams=4`, `max_new_tokens=100`)
4. The summary is decoded and displayed

##  Getting Started

```bash
# Clone the repo
git clone https://github.com/Mythilikalidhasan/<your-repo-name>.git
cd <your-repo-name>

# Install dependencies
pip install streamlit torch transformers

# Run the app
streamlit run app.py
```

> The model (~1.2 GB) downloads on the first run, so an internet connection is needed once.

## Project Structure

```
├── demo.py          # Streamlit app
├── requirements.txt  # Dependencies
└── README.md
```

##  Future Enhancements

- Handle long documents by chunking text and merging summaries
- Adjustable summary length (short / medium / detailed)
- Upload PDF/DOCX/TXT files for summarization
- Summarize from a URL (web article scraping)
- Multi-language support
- Choice of models (BART, T5, Pegasus) to compare outputs
- Copy / download summary button
- Deploy on Streamlit Community Cloud or Hugging Face Spaces

##  Author

**Mythili**
B.Sc. Computer Science with AI, SDNB Vaishnav College for Women
[GitHub](https://github.com/Mythilikalidhasan) · [LinkedIn](https://www.linkedin.com/in/mythili-k-392843378)
