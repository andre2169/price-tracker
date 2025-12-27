from app.service import obter_preco_atual


def main():
    url = (
        "https://www.mercadolivre.com.br/"
        "bicicleta-eletrica-scooter-bike-750w-104ah-led-2540kmh-cor-preto/"
        "p/MLB46639230"
    )

    preco = obter_preco_atual(url)
    print(f"Preço atual: R$ {preco}")


if __name__ == "__main__":
    main()
