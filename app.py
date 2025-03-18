import streamlit as st
import requests
from utils import summarize_text, analyze_sentiment, text_to_speech

API_URL = "https://newsapi.org/v2/everything"
API_KEY = "df0f1798a59e459989ef80fea179c2de"

st.title("📰 News Summarization & Sentiment Analysis with Hindi TTS")

company = st.text_input("Enter a company name:")

if st.button("Get News Summary"):
    if company:
        params = {"q": company, "apiKey": API_KEY, "language": "en"}
        response = requests.get(API_URL, params=params)

        if response.status_code == 200:
            articles = response.json().get("articles", [])[:10]  # Fetch 10 news articles

            if articles:
                # Combine all titles and descriptions
                text = ". ".join([f"{article['title']} - {article['description']}" for article in articles if article['description']])
                
                summary = summarize_text(text)  # Summarize text
                sentiment = analyze_sentiment(summary)

                st.subheader("📝 Summary (English):")
                st.write(summary)

                st.subheader("😊 Sentiment:")
                st.write(sentiment)

                text_to_speech(summary, "output.mp3")  # 🔥 Converts summary to Hindi TTS
                st.audio("output.mp3", format="audio/mp3")

            else:
                st.error("No articles found!")
        else:
            st.error("Error fetching news! Check API key.")
    else:
        st.warning("Please enter a company name.")
