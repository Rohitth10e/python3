from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client();



while True:
    user_input = input("enter-message: ");
    if user_input == "exit":
        break;
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
    )
    print("AI: ", response.text)