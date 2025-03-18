import nltk
import torch
from transformers import pipeline
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

# Download NLTK Resources
nltk.download("punkt")
nltk.download("vader_lexicon")

# Sentiment Analysis
def analyze_sentiment(text):
    from nltk.sentiment import SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    
    if score["compound"] >= 0.05:
        return "Positive 😊"
    elif score["compound"] <= -0.05:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Text Summarization
summarizer = pipeline("summarization")

def summarize_text(text):
    return summarizer(text, max_length=150, min_length=50, do_sample=False)[0]["summary_text"]

# Text-to-Speech (TTS)
def text_to_speech(text, filename):
    tts = gTTS(text, lang="hi")  # Hindi TTS
    tts.save(filename)

# Play Audio
def play_audio(file_path):
    if not os.path.exists(file_path):
        print(f"❌ Error: {file_path} not found!")
        return
    
    sound = AudioSegment.from_file(file_path, format="mp3")
    play(sound)
from gtts import gTTS
from googletrans import Translator

translator = Translator()

def text_to_speech(text, filename):
    hindi_text = translator.translate(text, src="en", dest="hi").text  # 🔥 English to Hindi
    tts = gTTS(text=hindi_text, lang="hi", slow=False)  # Hindi TTS
    tts.save(filename)
