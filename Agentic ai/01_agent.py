import json

from openai import OpenAI
from dotenv import load_dotenv
import requests
load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = '''
You can call a tool if required from the list of available tools
Output JSON Format:"
                 {"step":"START" | "PLAN" | "OUTPUT" | "TOOL", "content": "string"}
Available tools:
- get_weather(city: str): Take city name as input and return relevant weather of that particular city

Example 1:
START: What is the weather of Banglore?
PLAN: {"step":"PLAN", "content":"seems like user is interested in getting weather of banglore in India"}
PLAN: {"step":"PLAN", "content": "Let's see if we have any available tool from the list of available tools"}
PLAN: {"step":"PLAN", "content": "I need to call get_weather tool as banglore as input for city"}
PLAN: {"step":"TOOL", "content": "banglore"}
OUTPUT: {"step":"OUTPUT", "content": "string"}

            '''

def get_weather(city : str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong"

def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": user_query}
        ]
    )

    print(f"🤖: {response.choices[0].message.content}")

# main()
print(get_weather("goa"))
message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

# message_history.append({"role": "system", "content": SYSTEM_PROMPT})

while True:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type":"json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "system", "content": raw_result})

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "TOOL":
        tool_to_call = parsed_result.get("tool")
        tool_input = parsed_result.get("input")
        print(f"🔨: {tool_to_call} {tool_input}")
        continue
    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        continue