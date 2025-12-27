def limpar_preco(preco_texto: str) -> float:
    """
    Converte um preço em formato brasileiro para float.

    Exemplos:
    "5.200" -> 5200.0
    "1.500,90" -> 1500.90
    "R$ 3.999,99" -> 3999.99
    """

    preco = preco_texto.replace("R$", "")
    preco = preco.replace(".", "")
    preco = preco.replace(",", ".")
    return float(preco.strip())
