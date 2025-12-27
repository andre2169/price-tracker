import logging
from app.service import verificar_preco
from app.config import URL_PRODUTO


def main():
    logging.info("Iniciando verificação de preço")

    verificar_preco(URL_PRODUTO)

    logging.info("Finalizando execução")


if __name__ == "__main__":
    main()
