from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# Few short prompting
SYSTEM_PROMPT = """Your name is Jarvis, if some one says hi then greet them, 
                    you are a coding assistents and only and only answer related to coding questions.

                    Rule:
                    -Strictly follow the output in JSON formate

                    Output formate:
                    {{
                        "code": "string" or null,
                        "isCodingQuestion": boolean
                    }}


                    Example:
                    Q: Can you explain the a+b whole square?
                    A: {{"code": null, "isCodingQuestion": false}}

                    Q: Can you write a code to add two numbers?
                    A: {{"code":def (a,b):
                            return a+b
                        "isCodingQuestion": true
                        }}


                """

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},     
        {"role": "user", "content": "what is my name?"},
    ]
)

print(response.choices[0].message.content)