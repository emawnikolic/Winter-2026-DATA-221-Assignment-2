# Question 9

import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Machine_learning"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Request failed:", response.status_code)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

content = soup.find("div", id="mw-content-text").find("div", class_="mw-parser-output")

table = None
for tbl in content.find_all("table", class_="wikitable"):
    rows = tbl.find_all("tr")
    data_rows = [r for r in rows if r.find_all(["td", "th"])]
    if len(data_rows) >= 3:
        table = tbl
        break

if not table:
    print("No table with at least 3 rows found")
    exit()

header_row = table.find("tr")
headers = []
if header_row.find_all("th"):
    headers = [th.get_text(strip=True) for th in header_row.find_all("th")]
else:
    first_data_row = table.find("tr")
    col_count = len(first_data_row.find_all("td"))
    headers = [f"col{i+1}" for i in range(col_count)]

rows_data = []
for tr in table.find_all("tr"):
    cells = tr.find_all(["td", "th"])
    if not cells:
        continue
    row = [cell.get_text(strip=True) for cell in cells]
    # Pad missing cells
    if len(row) < len(headers):
        row += [""] * (len(headers) - len(row))
    rows_data.append(row)

with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows_data[1:])

print(f"Table saved to wiki_table.csv with {len(rows_data)-1} rows")
