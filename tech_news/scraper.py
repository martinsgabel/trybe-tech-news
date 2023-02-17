# Requisito 1
from parsel import Selector
import requests
from requests.exceptions import ConnectTimeout, HTTPError
import time


def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
    except (ConnectTimeout, HTTPError):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news_urls = []
    for news in selector.css("main > div > div > div"):
        link = news.css(
            "article > div > div:nth-child(2) > header > h2 > a ::attr(href)"
        ).get()
        news_urls.append(link)
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    try:
        next_page = selector.css("a.next.page-numbers ::attr(href)").get()
    except requests.RequestException:
        return None
    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
