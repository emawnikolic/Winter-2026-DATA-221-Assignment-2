#  Question 8

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

# Send request
response = requests.get(url, headers=headers)

# Check request success
if response.status_code != 200:
    print("Failed to retrieve page:", response.status_code)
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find real article content
content = soup.find("div", id="mw-content-text")
if content:
    content = content.find("div", class_="mw-parser-output")

if not content:
    print("Main content not found")
    exit()

exclude_words = ["References", "External links", "See also", "Notes"]

headings = []

# Extract headings
for h2 in content.find_all("h2"):

    span = h2.find("span", class_="mw-headline")

    if span:
        text = span.get_text().strip()
    else:
        text = h2.get_text().strip()

    # Remove edit text
    text = text.replace("[edit]", "").replace("Edit", "").strip()

    # Filter unwanted headings (case-insensitive)
    if not any(word.lower() in text.lower() for word in exclude_words):
        headings.append(text)

# Save to file
with open("headings.txt", "w", encoding="utf-8") as f:
    for h in headings:
        f.write(h + "\n")

print("Saved", len(headings), "headings to headings.txt")
