from app.service import verificar_preco
from app.config import URL_PRODUTO


def main():
    if verificar_preco(URL_PRODUTO):
        print("🔥 Preço abaixo do alvo!")
    else:
        print("Preço ainda acima do alvo.")


if __name__ == "__main__":
    main()
