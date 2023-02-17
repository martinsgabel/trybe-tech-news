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
    except (ConnectTimeout, HTTPError, requests.ReadTimeout):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    news_urls = []
    for news in selector.css("div.archive-wrap > div > article"):
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
    selector = Selector(html_content)

    url = selector.css("head > link:nth-child(10) ::attr(href)").get()
    title = selector.css("h1.entry-title ::text").get().strip()
    timestamp = selector.css("li.meta-date ::text").get()
    writer = selector.css("a.url ::text").get()
    readind_time = (
        selector.css("li.meta-reading-time ::text").get().split(" ")[0]
    )
    summary = "".join(selector.css(
        "div.entry-content > p:nth-of-type(1) *::text"
    ).getall()).strip()
    category = selector.css("span.label ::text").get()

    news_dict = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "readind_time": int(readind_time),
        "summary": summary,
        "category": category,
    }

    return news_dict


# Requisito 5
def get_tech_news(amount):
    site_html = fetch("https://blog.betrybe.com")
    news_url_list = []
    scrapped_news_list = []
    while len(news_url_list) < amount:
        scrape_updates(site_html)
        link_list = scrape_next_page_link(site_html)
        news_url_list.append(link_list)

    for index in range(amount):
        news_html = fetch(news_url_list[index])
        single_scrapped_news = scrape_news(news_html)
        scrapped_news_list.append(single_scrapped_news)

    return scrapped_news_list
