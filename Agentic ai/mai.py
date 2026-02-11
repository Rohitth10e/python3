# from openai import OpenAI
# from dotenv import load_dotenv
# load_dotenv()
#
# client = OpenAI()
# import os
# print(os.getenv("OPENAI_API_KEY"))
#
# def main():
#     user_query = input(">")
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o",
#             messages=[
#                 {"role": "user", "content": user_query}
#             ]
#         )
#         print(f"🤖: {response.choices[0].message.content}")
#     except Exception as e:
#         print(f"Error: {e}")
#
# if __name__ == "__main__":
#     main()

from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def main():
    user_query = input(">")
    # models = client.models.list()
    # for m in models:
    #     print(m.name)

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_query
        )
        print(f"🤖: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()