from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase base abstracta para las entidades del sistema."""

    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")
        self._identificador = str(identificador)

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def mostrar_informacion(self):
        """Cada entidad concreta define cómo mostrar su información."""
        raise NotImplementedError
