
from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase base abstracta para las entidades del sistema."""

    def __init__(self, identificador):
        if identificador is None or not str(identificador).strip():
            raise ValueError("El identificador es obligatorio.")

        self._identificador = str(identificador).strip()

    @property
    def identificador(self):
        """Permite consultar el identificador."""
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """Cada entidad concreta define cómo mostrar su información."""
        pass

