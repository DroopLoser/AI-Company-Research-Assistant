import re
from bs4 import BeautifulSoup


def clean_text(html):

    soup = BeautifulSoup(html, "html.parser")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()

    text = soup.get_text(separator=" ", strip=True)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text

import re

def extract_phone(text):

    pattern = r"(\+?\d[\d\s\-\(\)]{8,}\d)"

    matches = re.findall(pattern, text)

    return list(set(matches))

def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    emails = re.findall(pattern, text)

    return list(set(emails))

def extract_email(text):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    emails = re.findall(pattern, text)

    return list(set(emails))