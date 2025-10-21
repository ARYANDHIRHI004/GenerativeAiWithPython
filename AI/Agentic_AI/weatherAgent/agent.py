
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# chain of thought
SYSTEM_PROMPT = """
    You are an weather agent who calls a TOOLS to get the current weather
    You are an expert AI assistent in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    You need to call the available TOOLS to get the current weather of a city.
    Once you think enough PLAN has been done, finally you give an OUTPUT.

    Rules:
    -Strictly follow the given JSON output format
    -Only run one step at a time
    -The sequence of step is START(where user gives an input), PLAN(This step can be performed multiple times) and finally OUTPUT(which is going to the displayed to the user)

    Output JSON Formate:
    {"step": "START" | "PLAN" | "OUTPUT" | "TOOLS", "content": "string", "tool":"string", "input":"string"}

    Availablr Tools:
    -get_weather: Takse city name as an input and return the weather of the city.

    Example:
    START: Hey, whatt is the weather of delhi
    PLAN: {"step": "PLAN", "content":"Seems like you are intrested to know the weather of the delhi in india"}
    PLAN: {"step": "PLAN", "content":"To get the current weather,I have to call the Tools"}
    PLAN: {"step": "PLAN", "content":"I need to call get_weather for delhi as input"}
    TOOL: {"step": "TOOL", "tool":"get_weather" "input":"delhi"}
    OBSERVE: {"step": "OBSERVE", "tool":"get_weather", "input":"delhi", "output":"The weather of delhi is seems like little cloudy with 30 degree celcius"}
    OUTPUT: {"step": "OUTPUT", "content":"The current weather of delhi is 20 degree celcius with cloudy sky"}

"""

def get_weather(city):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}."

    return "Something went wrong."


available_tools = {
    "get_weather": get_weather
}

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_quere = input("🧨> ")
message_history.append({"role": "user", "content": user_quere})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result},)
    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🎁", parsed_result.get("content"))
        continue
    
    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "TOOL":
        tool_to_call = parsed_result.get("tool")
        city_input = parsed_result.get("input")
        tool_response = available_tools[tool_to_call](city_input)
        print(f"🔧 {tool_to_call}({city_input}) = {tool_response}")
        message_history.append({"role": "developer", "content": json.dumps(
            {"step":"OBSERVE", "tool":tool_to_call, "input":city_input, "output":tool_response}
        )})
        continue
    
    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break

print("\n\n\n")

