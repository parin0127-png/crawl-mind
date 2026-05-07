from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import requests

def playwright_scraper(url):
    h1_list = []
    h2_list = []
    h3_list = []

    with sync_playwright() as p:
        website = p.chromium.launch(headless = True,
        args=[
        "--no-sandbox",
        "--disable-blink-features=AutomationControlled",
        "--disable-dev-shm-usage"
    ])
        page = website.new_page()
        page.set_extra_http_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
        page.set_default_timeout(60000)
        page.goto(url, wait_until = "domcontentloaded")
        page.wait_for_timeout(5000)
        html = page.content()
        website.close()

    soup = BeautifulSoup(html, "lxml")
    title = soup.find("title")
    h1 = soup.find_all("h1")
    h2 = soup.find_all("h2")
    h3 = soup.find_all("h3")
    meta_tag = soup.find(attrs = {"name" : "description"})
    meta = meta_tag.get("content") if meta_tag else None
    img = soup.find_all("img")

    if h1:
        for h in h1:
            h1_list.append(h.get_text(strip = True))
    if h2:
        for h in h2:
            h2_list.append(h.get_text(strip = True))
    if h3:
        for h in h3:
            h3_list.append(h.get_text(strip = True))

    total = 0
    missing_alt = 0
    if img:
        for i in img:
            total += 1

            if not i.get("alt"):
                missing_alt += 1
    words = soup.get_text().split()

    return {
        "url" : url,
        "title" : title.get_text() if title else "> Not found anything",
        "h1" : h1_list,
        "h2" : h2_list,
        "h3" : h3_list,
        "meta_description" : meta if meta else "",
        "total" : total,
        "missing_alt" : missing_alt,
        "word_count" : len(words)
    }


def web_scraper(url):
    h1_list = []
    h2_list = []
    h3_list = []

    fetch = requests.get(url, headers =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(fetch.text, "lxml")
    title = soup.find("title")
    h1 = soup.find_all("h1")
    h2 = soup.find_all("h2")
    h3 = soup.find_all("h3")
    meta_tag = soup.find(attrs = {"name" : "description"})
    meta = meta_tag.get("content") if meta_tag else None
    img = soup.find_all("img")

    if h1:
        for h in h1:
            h1_list.append(h.get_text(strip = True))
    if h2:
        for h in h2:
            h2_list.append(h.get_text(strip = True))
    if h3:
        for h in h3:
            h3_list.append(h.get_text(strip = True))

    total = 0
    missing_alt = 0
    if img:
        for i in img:
            total += 1

            if not i.get("alt"):
                missing_alt += 1
    words = soup.get_text().split()

    if len(words) < 50:
        return playwright_scraper(url)
    return {
        "url" : url,
        "title" : title.get_text() if title else "> Not found anything",
        "h1" : h1_list,
        "h2" : h2_list,
        "h3" : h3_list,
        "meta_description" : meta if meta else "",
        "total" : total,
        "missing_alt" : missing_alt,
        "word_count" : len(words)
    }


