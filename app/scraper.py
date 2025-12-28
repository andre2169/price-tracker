import requests
import logging
from bs4 import BeautifulSoup
from app.config import HEADERS


def buscar_preco(url: str) -> str:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    preco = soup.select_one("p.price_color")

    if not preco:
        raise ValueError("Preço não encontrado no HTML")

    return preco.text.replace("£", "").strip()