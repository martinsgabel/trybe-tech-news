# Requisitos 11 e 12
import sys

from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_category,
    search_by_date,
)
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_categories


def search_quantity():
    input_value = int(input("Digite quantas notícias serão buscadas"))
    print(get_tech_news(input_value))


def search_title():
    input_value = input("Digite o titulo:")
    print(search_by_title(input_value))


def search_data():
    input_value = input("Digite a data no formato aaaa-mm-dd")
    print(search_by_date(input_value))


def search_category():
    input_value = input("Digite a categoria:")
    print(search_by_category(input_value))


def search_top_5():
    return top_5_categories()


def analyzer_menu():
    """Seu código deve vir aqui, and it will"""
    menu_text = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair. ",
    )

    options = {
        "0": search_quantity,
        "1": search_title,
        "2": search_data,
        "3": search_category,
        "4": search_top_5,
    }

    try:
        if options == "5":
            print("Encerrando script")
        options[menu_text]()
    except (KeyError, ValueError):
        return print("Opção inválida", file=sys.stderr)

    pass
