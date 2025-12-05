from dotenv import load_dotenv
import os

load_dotenv()
key = os.environ.get("LANGCHAIN_API_KEY")
genai_key = os.environ.get("GOOGLE_API_KEY")
