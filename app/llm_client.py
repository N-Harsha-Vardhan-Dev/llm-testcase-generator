import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# print(os.getenv("GOOGLE_API_KEY"))
def call_llm(prompt: str) -> str:
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise RuntimeError("GOOGLE_API_KEY not set")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",  # ✅ updated model
        contents=prompt
    )

    return response.text.strip()
