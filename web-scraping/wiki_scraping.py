import csv
import time
from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://terraria.wiki.gg"
BOSSES_URL = f"{BASE_URL}/wiki/Bosses"
ROBOTS_URL = f"{BASE_URL}/robots.txt"
HEADERS = {
    "User-Agent": "is310-course-scraper/1.0 (student project; hongjuj2@illinois.edu)"
}
REQUEST_DELAY = 2.0
OUTPUT_CSV = "terraria_bosses.csv"

GROUPS = {
    "Pre-Hardmode bosses": "pre-hardmode",
    "Hardmode bosses": "hardmode",
    "Event bosses": "event",
    "Special world seed-exclusive boss": "special_seed",
}

robots = RobotFileParser()
def load_robots():
    response = requests.get(ROBOTS_URL, headers=HEADERS, timeout=30)
    time.sleep(REQUEST_DELAY)
    if response.status_code != 200:
        raise SystemExit("Could not read robots.txt. Stopping.")
    robots.parse(response.text.splitlines())


def fetch_soup(url):
    if not robots.can_fetch(HEADERS["User-Agent"], url):
        print(f"Not allowed by robots.txt: {url}")
        return None

    response = requests.get(url, headers=HEADERS, timeout=30)
    time.sleep(REQUEST_DELAY)

    if response.status_code != 200:
        print(f"Could not download {url}: HTTP {response.status_code}")
        return None

    return BeautifulSoup(response.text, "html.parser")

def scrape_boss_list(soup):
    bosses = []
    if soup is None:
        return bosses

    content = soup.select_one("#mw-content-text .mw-parser-output")
    group = None

    for heading in content.find_all(["h2", "h3"]):
        name = heading.get_text(strip=True).removesuffix("[edit]").strip()

        if heading.name == "h2":
            group = GROUPS.get(name)  
            continue

        if group is None:
            continue

        link = heading.find_next("a", title=name, href=True)
        if link is None:
            continue

        bosses.append({
            "boss": name,
            "boss_group": group,
            "boss_url": urljoin(BASE_URL, link["href"]),
        })

    return bosses


def get_internal_links(content):
    links = []
    for link in content.find_all("a", href=True):
        href = link["href"]
        if href.startswith("/wiki/") and "#" not in href and "?" not in href:
            links.append(href)
    return links


def analyze_boss(boss):
    record = boss.copy()
    record["word_count"] = 0
    record["character_count"] = 0
    record["internal_link_count"] = 0
    record["unique_internal_link_count"] = 0

    soup = fetch_soup(boss["boss_url"])
    if soup is None:
        return record

    content = soup.select_one("#mw-content-text .mw-parser-output")
    if content is None:
        return record

    text = content.get_text(" ", strip=True)
    links = get_internal_links(content)

    record["word_count"] = len(text.split())
    record["character_count"] = len(text)
    record["internal_link_count"] = len(links)
    record["unique_internal_link_count"] = len(set(links))
    return record


def save_csv(records, output_path):
    if not records:
        print("No records to save.")
        return
    with open(output_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)


def print_group_averages(records):
    groups = {}
    for record in records:
        groups.setdefault(record["boss_group"], []).append(record)

    print("\ngroup          n   words   links  unique")
    for group, rows in groups.items():
        n = len(rows)
        words = sum(row["word_count"] for row in rows) / n
        links = sum(row["internal_link_count"] for row in rows) / n
        unique = sum(row["unique_internal_link_count"] for row in rows) / n
        print(f"{group:<13}{n:>3}{words:>8.0f}{links:>8.0f}{unique:>8.0f}")

def main():
    load_robots()

    bosses = scrape_boss_list(fetch_soup(BOSSES_URL))
    print(f"Found {len(bosses)} bosses.")

    results = []
    for number, boss in enumerate(bosses, start=1):
        print(f"{number}/{len(bosses)} {boss['boss']}")
        results.append(analyze_boss(boss))

    save_csv(results, OUTPUT_CSV)
    print_group_averages(results)
    print(f"\nSaved {len(results)} rows to {OUTPUT_CSV}")

if __name__ == "__main__":
    main()