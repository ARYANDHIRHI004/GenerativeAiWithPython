from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# chain of thought
SYSTEM_PROMPT = """
    You are an expert AI assistent in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you give an OUTPUT.

    Rules:
    -Strictly follow the given JSON output format
    -Only run one step at a time
    -The sequence of step is START(where user gives an input), PLAN(T hat cba be multiple times) and finally OUTPUT(which is going to the displayed to the user)

    Output JSOn Formate:
    {"step": "START" | "PLAN" | "OUTPUT", "content": "string"}

    Example:
    START: Hey, Can you soolve 2+3*5/10
    PLAN: {"step": "PLAN", "content":"Seems like you are intrested in maths problem"}
    PLAN: {"step": "PLAN", "content":"Yes, Looking at the problem, we should apply BODMAS method"}
    PLAN: {"step": "PLAN", "content":"first we multiply 3*5 which is 15"}
    PLAN: {"step": "PLAN", "content":"Now we will divide 15/10  which is 1.5"}
    PLAN: {"step": "PLAN", "content":"and then we will add 2 + 1.5, after adding we get 3.5"}
    OUTPUT: {"step": "OUTPUT", "content":"3.5"}

"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},     
        {"role": "user", "content": "write a code to find factorial of any number"},
        {"role": "assistant", "content": json.dumps({"step": "START", "content": "The user wants a code to find the factorial of any number."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN", "content": "The user wants a code to calculate the factorial of any given number. I need to provide a function that takes an integer as input and returns its factorial."})},
        {"role": "assistant", "content": json.dumps({"step": "PLAN","content": "I will define a function that handles the factorial calculation. I should also consider edge cases like negative numbers and zero. The factorial of 0 is 1. Factorials are not defined for negative numbers. For positive integers, I'll use a loop or recursion to multiply all integers from 1 up to the given number."})},
        
    ]
)

print(response.choices[0].message.content)