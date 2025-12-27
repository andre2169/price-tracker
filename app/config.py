import os
from dotenv import load_dotenv
import logging
from pathlib import Path


HEADERS = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "pt-BR,pt;q=0.9"
}

load_dotenv()

URL_PRODUTO = os.getenv("URL_PRODUTO")
PRECO_MAXIMO = float(os.getenv("PRECO_ALVO"))

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "price_tracker.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)