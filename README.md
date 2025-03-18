# 📰 AI News Summarization & Sentiment Analysis

This project fetches real-time news articles, summarizes them, analyzes sentiment, and provides Hindi translation with text-to-speech (TTS) support.

## 📌 Features
- Fetch news from **NewsAPI**
- Summarize articles using **NLTK**
- Analyze sentiment (Positive/Negative/Neutral)
- Translate summaries to **Hindi**
- Generate **Text-to-Speech (TTS)** audio

## 🛠 Setup & Installation
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
pip install -r requirements.txt
python app.py
🔗 API Endpoints
Fetch News & Sentiment Analysis
GET /fetch_news?company=Tesla
Example Response:
json
Copy
Edit
{
    "Company": "Tesla",
    "Articles": [
        {
            "Title": "Tesla Stock Jumps",
            "Summary": "Tesla reported strong earnings...",
            "Sentiment": "Positive"
        }
    ]
}
📂 Project Structure
bash
Copy
Edit
nstsa/
│── api.py           # API functions
│── app.py           # Main script
│── utils.py         # Utility functions
│── requirements.txt # Dependencies
│── README.md        # Documentation
