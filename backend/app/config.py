# backend/app/config.py

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///pre_consultation.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
