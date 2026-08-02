import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def ask_ai(prompt, model="nvidia/nemotron-3-ultra-550b-a55b:free"):

    response = client.chat.completions.create(

        model=model,

        messages=[
            {
                "role": "system",
                "content":
                "You are a professional company research analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

    )

    return response.choices[0].message.content