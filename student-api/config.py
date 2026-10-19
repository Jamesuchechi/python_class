import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Student API")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"