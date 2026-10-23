# Web Scraping on Terraria Wiki Bosses
| File | Description |
|---|---|
| `wiki_scraping.py` | Scraper (requests + BeautifulSoup) |
| `terraria_bosses.csv` | Output data, one row per boss |
| `first_web_scraper.py` | In-class exercise |

To run, put this in your terminal:

```
python -m pip install requests beautifulsoup4
python wiki_scraping.py
```

## Wiki and research question

I chose the [Terraria Wiki](https://terraria.wiki.gg), the official community wiki for the game Terraria. It left Fandom.com for independent hosting on wiki.gg, and its pages follow a consistent structure that is easy to scrape.

**"Does the Terraria Wiki document progression bosses more heavily than optional event bosses?"**

The wiki's [Bosses](https://terraria.wiki.gg/wiki/Bosses) page sorts all 33 bosses into pre-Hardmode, Hardmode, event, and special-seed groups. My scraper reads that page (level 1), then visits each boss's page (level 2) and records its word count, character count, total internal links, and unique internal links. Comparing these groups shows where volunteer documentation is concentrated, which could interest researchers studying fan labor and what parts of a game a community treats as worth explaining.

## robots.txt

robots.txt: <https://terraria.wiki.gg/robots.txt>

- **Permits:** all user agents may crawl `/` (`Allow: /`), so ordinary article pages are open. Content may be used for search and reference, but not for AI training (`ai-train=no`). `api.php`, `index.php`, edit/history/diff URLs (`?action=`, `?oldid=`), search, `Special:`, `File:`, and `User:` pages. It also fully blocks AI-training bots, SEO bots, and flooding tools like recursive `wget` and `Scrapy`, and warns that irresponsible automated traffic may be restricted.

My scraper only requests allowed article pages, checks every URL against robots.txt in code, sends an honest User-Agent, waits 2 seconds between requests, and does not parse pages that do not return 200. It collects only counts, not article text.

## Results

| Group | Bosses | Avg. words | Avg. links | Avg. unique links |
|---|---:|---:|---:|---:|
| Pre-Hardmode | 8 | 4,302 | 974 | 694 |
| Hardmode | 10 | 4,646 | 907 | 646 |
| Event | 14 | 3,683 | 907 | 639 |
| Special seed | 1 | 2,546 | 703 | 581 |

Event boss pages are about 15 to 20 percent shorter than progression boss pages, but their link counts are nearly the same.

## Reflection
For this project, I wanted to know which bosses the community thinks are worth explaining. What I measured is the length and link counts of 33 pages on one day. A long page may reflect interest, but it also reflects complexity since a boss with several phases and many drops has more facts to list. Much of each page also comes from shared templates like infoboxes and navigation boxes. Each page has 600 to 700 unique links, which is far more than anyone writes by hand, so these counts partly measure the wiki's formatting rather than editors' choices. Someone would be wrong to conclude that a boss with a longer page is more popular or important to players, or that event bosses are less loved since some of their information may live on their event's page