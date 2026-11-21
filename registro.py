# logging permite guardar eventos y errores en un archivo, path construye su ruta.
import logging
from pathlib import Path


# Define logs.txt en la misma carpeta donde se encuentra este modulo
RUTA_LOG = Path(__file__).with_name("logs.txt")


# Configura el archivo, el nivel de registro y el formato de cada mensaje
logging.basicConfig(filename=RUTA_LOG, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", encoding="utf-8")


# Guarda una operación que se completo correctamente
def registrar_evento(mensaje):
    # Registra operaciones realizadas correctamente
    logging.info(mensaje)


# Guarda el mensaje de error y, si se proporciona, también la información técnica
def registrar_error(mensaje, error=None):
    #Registra errores y, cuando existe, su información técnica

    if error is not None:
        logging.error("%s: %s", mensaje, error, exc_info=(type(error), error, error.__traceback__))
    else:
        logging.error(mensaje)
