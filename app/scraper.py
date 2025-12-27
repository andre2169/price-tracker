import requests
from bs4 import BeautifulSoup
from app.config import HEADERS


def buscar_preco(url: str) -> str:
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # seletor inicial
    preco = soup.select_one("span.andes-money-amount__fraction")

    if not preco:
        raise ValueError("Preço não encontrado no HTML")

    return preco.text
