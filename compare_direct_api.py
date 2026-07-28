import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

print("=" * 50)
print("Direct OpenAI API")
print("=" * 50)

question = input("Enter your question: ")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful teacher."
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

print("\nAI Response\n")
print(response.choices[0].message.content)