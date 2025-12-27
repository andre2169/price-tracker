from app.scraper import buscar_preco
from app.parser import limpar_preco
from app.config import PRECO_ALVO


def verificar_preco(url: str) -> bool:
    """
    Verifica se o preço atual é menor ou igual ao preço alvo.
    """
    preco_texto = buscar_preco(url)
    preco_atual = limpar_preco(preco_texto)

    return preco_atual <= PRECO_ALVO
