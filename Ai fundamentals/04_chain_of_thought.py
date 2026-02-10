import os

from google import genai
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta",
)

SYSTEM_PROMPT = '''You're an expert AI assistant in resolving user queries using chain of thoughts. You work
on start, Plan and output steps. You need to first plan what needs to be done. The plan can be multiple steps once you think plans are done provide output based on:

1. strictly follow the given json output format
2. only run step at a time
3. the sequence of steps is start where user gives an input plan that can be multiple times and finally the output which is going to be displayed to the user

output format:
{step:START | PLAN | OUTPUT , content: string}
'''

message_history = [
{"role": "system", "content": SYSTEM_PROMPT}
]

user_query = input("👉🏼")
message_history.append({"role":"user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type":"json_object"},
        messages= message_history,)
    raw_result = response.choices[0].message.content
    message_history.append({"role":"assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)
    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        continue
    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        continue


