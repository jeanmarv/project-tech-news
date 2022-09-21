from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    titles = []
    title_url = search_news({"title": {"$regex": title, "$options": "i"}})

    for itens in title_url:
        titles.append((itens["title"], itens["url"]))

    return titles


# Requisito 7
def search_by_date(date):
    news_by_date = []
    try:
        date_str = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        results = search_news({"timestamp": date_str})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        for itens in results:
            news_by_date.append((itens["title"], itens["url"]))
        return news_by_date


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
