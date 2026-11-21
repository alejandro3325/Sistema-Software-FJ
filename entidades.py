# ABC permite definir una clase abstracta; abstractmethod obliga a implementar un método en las clases hijas.
from abc import ABC, abstractmethod


# Entidad es la clase base común para clientes, servicios y reservas.
class Entidad(ABC):
    #Clase base abstracta para las entidades del sistema

# Comprueba que el identificador no esté vacío y lo guarda como texto.
    def __init__(self, identificador):
        if identificador is None or not str(identificador).strip():
            raise ValueError("El identificador es obligatorio.")

        self._identificador = str(identificador).strip()

# Propiedad de solo lectura para consultar el identificador.
    @property
    def identificador(self):
        #Permite consultar el identificador
        return self._identificador

# Cada clase concreta debe definir su propia forma de mostrar información.
    @abstractmethod
    def mostrar_informacion(self):
        #Cada entidad concreta define cómo mostrar su información
        pass
