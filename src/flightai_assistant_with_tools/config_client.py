import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

llm_base_url = os.getenv("GROQ_BASE_URL")
llm_model_name= os.getenv("GPT_MODEL")
llm_api_key = os.getenv("GROQ_API_KEY")

client = OpenAI(api_key=llm_api_key, base_url=llm_base_url)