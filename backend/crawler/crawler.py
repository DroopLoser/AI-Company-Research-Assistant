import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


IGNORE_WORDS = [
    "login",
    "signup",
    "register",
    "admin",
    "cart",
    "checkout"
]


IMPORTANT_KEYWORDS = [
    "about",
    "product",
    "service",
    "solution",
    "pricing",
    "contact"
]


visited_urls = set()


def is_valid_url(url):

    for word in IGNORE_WORDS:
        if word in url.lower():
            return False

    return True



def extract_links(url, html):

    soup = BeautifulSoup(html, "html.parser")

    links = []

    for link in soup.find_all("a", href=True):

        full_url = urljoin(
            url,
            link["href"]
        )

        if is_valid_url(full_url):

            links.append(full_url)

    return links



def extract_text(html):

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text(
        separator=" ",
        strip=True
    )

    return text



def crawl_website(start_url, max_pages=7):

    global visited_urls

    queue = [start_url]

    pages = []


    while queue and len(pages) < max_pages:

        url = queue.pop(0)


        if url in visited_urls:
            continue


        visited_urls.add(url)


        try:

            response = requests.get(
                url,
                timeout=10,
                headers={
                    "User-Agent":"Mozilla/5.0"
                }
            )


            html = response.text


            text = extract_text(html)


            pages.append({
                "pages": [
                    {
                         "url": "...",
                         "content": "..."
                    }
                ],
                 "contact": {
                     "phones": [...],
                      "emails": [...]
                  }
            })


            links = extract_links(
                url,
                html
            )


            for link in links:

                if any(
                    keyword in link.lower()
                    for keyword in IMPORTANT_KEYWORDS
                ):
                    queue.append(link)


        except Exception as e:

            print(
                "Failed:",
                url,
                e
            )


    return pages