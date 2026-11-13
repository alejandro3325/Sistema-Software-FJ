import logging
from pathlib import Path

RUTA_LOG = Path(__file__).with_name("logs.txt")

logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def registrar_evento(mensaje):
    logging.info(mensaje)

def registrar_error(mensaje):
    logging.exception(mensaje)
