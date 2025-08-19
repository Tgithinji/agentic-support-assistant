import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Get API keys safely
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("❌ Missing OPENAI_API_KEY. Please set it in your .env file.")
