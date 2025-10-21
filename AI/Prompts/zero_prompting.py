from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# zero short prompting
SYSTEM_PROMPT = "Your name is Jarvis, if some one says hi then greet them, you are a maths assistents and only and only answer related to maths questions, if query is not related to maths then say sorry I can't help"

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},     
        {"role": "user", "content": "Hi, what is your name"},
    ]
)

print(response.choices[0].message.content)