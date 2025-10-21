from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are a maths assistents and only and only answer related to maths questions, if query is not related to maths then say sorry I can't help"},     
        {"role": "user", "content": "Hello! write a code to print hello world in js "},
    ]
)

print(response.choices[0].message.content)