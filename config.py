import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_client():

       my_api_key = os.getenv("GROQ_API_KEY")

       if not my_api_key:
             raise ValueError("API key not found.")

       client = OpenAI(api_key = my_api_key, 
                       base_url='https://api.groq.com/openai/v1')

       return client

   


