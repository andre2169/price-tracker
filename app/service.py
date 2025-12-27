from app.scraper import buscar_preco
from app.parser import limpar_preco


def obter_preco_atual(url: str) -> float:
    """
    Orquestra a obtenção do preço atual de um produto.
    """
    preco_texto = buscar_preco(url)
    preco_float = limpar_preco(preco_texto)
    return preco_float
