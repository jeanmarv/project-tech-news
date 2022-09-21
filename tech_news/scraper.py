import requests
import time
import parsel
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(text=html_content)
    urls_news = selector.css("a.cs-overlay-link::attr(href)").getall()
    return urls_news


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(text=html_content)
    urls_news = selector.css("a.next.page-numbers::attr(href)").get()
    return urls_news


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = len(selector.css("div.comment-body").getall())
    summary = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()
    tags = selector.css("section.post-tags ul li a::text").getall()
    category = selector.css("div.meta-category span.label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "summary": summary,
        "comments_count": comments_count,
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    news_amount = []
    url = "https://blog.betrybe.com/"

    while len(news_amount) < amount:
        fetch_news_content = fetch(url)
        all_news = scrape_novidades(fetch_news_content)
        for itens in all_news:
            fetch_content = fetch(itens)
            news_summary = scrape_noticia(fetch_content)
            news_amount.append(news_summary)
            if len(news_amount) == amount:
                break
        url = scrape_next_page_link(fetch_news_content)

    create_news(news_amount)
    return news_amount
