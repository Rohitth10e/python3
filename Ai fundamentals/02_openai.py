from dotenv import load_dotenv
from openai import OpenAI;

load_dotenv()

client = OpenAI();

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content":"Hey there"}
    ]
);

print(response.choices[0].message.content)