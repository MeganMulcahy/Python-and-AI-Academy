import requests
from bs4 import BeautifulSoup
import json
import re
import datetime

url = 'https://archive.ics.uci.edu/datasets'

response = requests.get(url)
status = response.status_code
print(status) # 200 means the fetching was successful

content = response.content
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title)
print(soup.title.get_text())
# print(soup.body)

tables = soup.find_all('table')
print(f"Total tables found: {len(tables)}")

def scrape_presidents(url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"ERROR: HTTP {response.status_code}")
        return None
    
    # Parse HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the main presidents table
    # Look for the first <table class="wikitable"> after any heading with "Presidents"
    table = None
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        if 'president' in heading.get_text().lower():
            table = heading.find_next("table", class_="wikitable")
            if table:
                break

    if not table:
        print("Could not find the presidents table.")
        return None

    # Extract rows
    rows = table.find_all("tr")
    presidents = []

    for row in rows[1:]:  # Skip header row
        cells = row.find_all(["td", "th"])
        if len(cells) < 6:  # Skip malformed rows
            continue

        def get_text(cell):
            return " ".join(cell.stripped_strings).strip()

        # Extract portrait image
        portrait = ""
        img = cells[1].find("img") if len(cells) > 1 else None
        if img and img.get("src"):
            portrait = "https:" + img["src"]

        president = {
            "no": get_text(cells[0]).rstrip('.'),  # Remove period
            "name": re.sub(r"\s*\(.*?\).*|\[.*?\]", "", get_text(cells[2])).strip(), #\s*\(.*?\).* finds the space, the opening parenthesis, the dates inside, the closing parenthesis, and everything after it . \[.*?\] finds any leftover Wikipedia brackets like [a] or [19]
            "dates": re.sub(r"^.*?\((.*?)\).*|.*", r"\1", get_text(cells[2])).strip(), # This matches the entire string but captures the dates inside the parentheses using (.*?). Then, r"\1" replaces the whole sentence with only what was caught inside those parentheses.The |.* at the end is a safety net. If a row has no parentheses at all, it matches the whole string and deletes it, returning an empty string ""
            "term": get_text(cells[3]),
            "party": get_text(cells[4]),
            "election": get_text(cells[5]),
            "vice_president": get_text(cells[6]) if len(cells) > 6 else ""
        }
        if portrait:
            president["portrait"] = portrait

        presidents.append(president)

    # Build final data
    data = {
        "url": url,
        "title": "List of Presidents of the United States",
        "scraped_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "total_presidents": len(presidents),
        "presidents": presidents
    }

    # Save to JSON
    with open("presidents.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print("Data successfully saved!")
    
    return data

scrape_presidents()