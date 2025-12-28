import logging
from app.service import verificar_preco
from app.config import URL_PRODUTO


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


def main():
    logging.info("MAIN.PY EXECUTADO")
    logging.info("Iniciando verificação de preço")

    verificar_preco(URL_PRODUTO)

    logging.info("Finalizando execução")


if __name__ == "__main__":
    main()

