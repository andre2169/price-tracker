from app.service import obter_preco_atual
from app.config import URL_PRODUTO


def main():
    preco = obter_preco_atual(URL_PRODUTO)
    print(f"Preço atual: R$ {preco}")


if __name__ == "__main__":
    main()
