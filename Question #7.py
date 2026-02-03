# Question 7

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

session = requests.Session()

session.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer": "https://www.google.com/"
})

response = session.get(url)

if response.status_code != 200:
    print("Request failed with status code:", response.status_code)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("title").text
print("Page Title:", title)

content = soup.find("div", id="mw-content-text")

first_paragraph = ""

for p in content.find_all("p"):
    text = p.get_text().strip()
    if len(text) >= 50:
        first_paragraph = text
        break

print("\nFirst Paragraph (>= 50 characters):")
print(first_paragraph)
