
import logging
from pathlib import Path


RUTA_LOG = Path(__file__).with_name("logs.txt")


logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8
)


def registrar_evento(mensaje):
    """Registra operaciones realizadas correctamente."""
    logging.info(mensaje)


def registrar_error(mensaje, error=None):
    """Registra errores y, cuando existe, su información técnica."""

    if error is not None:
        logging.error(
            "%s: %s",
            mensaje,
            error,
            exc_info=(
                type(error),
                error,
                error.__traceback__
            )
        )
    else:
        logging.error(mensaje)

