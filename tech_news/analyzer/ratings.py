# Requisito 10
from collections import Counter
from tech_news.database import find_news


def top_5_categories():
    """Seu código deve vir aqui"""
    top_categories = []
    categories_list = []

    for news in find_news():
        categories_list.append(news["category"])

    categories_list = Counter(sorted(categories_list)).most_common(5)

    for category in categories_list:
        top_categories.append(category[0])

    return top_categories
