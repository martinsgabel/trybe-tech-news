# Requisito 7
from datetime import datetime
from tech_news.database import find_news, search_news


def search_by_title(title):
    """Seu código deve vir aqui"""
    return [
        (news["title"], news["url"])
        for news in find_news()
        if title.lower() in news["title"].lower()
    ]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        news_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    
    return [
        (news["title"], news["url"])
        for news in search_news({"timestamp": news_date})
    ]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    return [
        (news["title"], news["url"])
        for news in find_news()
        if category.lower() in news["category"].lower()
    ]
