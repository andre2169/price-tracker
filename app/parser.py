import re

def limpar_preco(preco: str) -> float:
    """
    Converte strings como:
    'R$ 5.177,00'
    'Â5177'
    '5.177'
    em float: 5177.0
    """

    if not preco:
        raise ValueError("Preço vazio ou None")

    # Remove qualquer coisa que não seja número ou separador
    preco_limpo = re.sub(r"[^\d,\.]", "", preco)

    # Se vier no formato brasileiro
    if "," in preco:
        preco_limpo = preco_limpo.replace(".", "").replace(",", ".")

    return float(preco_limpo)
