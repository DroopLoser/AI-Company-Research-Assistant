import os
import requests
from dotenv import load_dotenv

load_dotenv()


SERPER_API_KEY = os.getenv("SERPER_API_KEY")

SERPER_URL = "https://google.serper.dev/search"


def search_company(query: str):

    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "q": query
    }

    response = requests.post(
        SERPER_URL,
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        return {
            "error": "Search failed",
            "status": response.status_code
        }

    return response.json()