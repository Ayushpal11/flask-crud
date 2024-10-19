import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/user_db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'

class TestConfig(Config):
    MONGO_URI = 'mongodb://localhost:27017/test_db'
    TESTING = True