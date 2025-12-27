import logging
from app.scraper import buscar_preco
from app.parser import limpar_preco
from app.config import PRECO_MAXIMO


def verificar_preco(url: str) -> bool:
    """
    Regra de negócio:
    Retorna True se o preço atual for menor ou igual ao preço máximo definido.
    """
    preco_texto = buscar_preco(url)
    preco_atual = limpar_preco(preco_texto)

    logging.info(
        f"Preço atual: {preco_atual} | Preço máximo permitido: {PRECO_MAXIMO}"
    )

    if preco_atual <= PRECO_MAXIMO:
        logging.info("Preço abaixo do limite. Ação permitida.")
        return True

    logging.info("Preço acima do limite. Nenhuma ação tomada.")
    return False
