import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('API_KEY')
NEYRO_KEY = os.getenv('Api-Key-ney')