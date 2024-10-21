# backend/app/utils.py

import os
import openai
from google.cloud import speech
from textblob import TextBlob

from flask import current_app

def transcribe_speech(audio_content):
    """
    Transcribe speech to text using Google Cloud Speech-to-Text.
    """
    client = speech.SpeechClient()
    
    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,  # Ensure frontend sends LINEAR16
        sample_rate_hertz=16000,  # Ensure frontend sends 16000 Hz
        language_code="en-US"
    )
    
    response = client.recognize(config=config, audio=audio)
    
    transcripts = [result.alternatives[0].transcript for result in response.results]
    return ' '.join(transcripts)

def analyze_emotional_tone(text):
    """
    Analyze the emotional tone of the text using TextBlob.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

def generate_generative_response(prompt):
    """
    Generate a response using OpenAI's GPT model.
    """
    openai.api_key = current_app.config['OPENAI_API_KEY']
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the appropriate engine
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
