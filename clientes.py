# Importa herramientas para validar el formato del correo electronico
import re

# Importa la clase base de las entidades y la excepción para datos invalidos
from entidades import Entidad
from excepciones import DatosInvalidosError


# La clase cliente hereda el identificador y la estructura comun de entidad
class Cliente(Entidad):
    #Representa a un cliente de software FJ

# Inicializa el cliente y asigna sus datos mediante propiedades que los validan
    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

# La propiedad permite consultar el nombre almacenado
    @property
    def nombre(self):
        return self._nombre

# Valida que el nombre sea texto y tenga al menos dos caracteres
    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise DatosInvalidosError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = valor.strip()

# La propiedad permite consultar el correo electronico
    @property
    def correo(self):
        return self._correo

# Comprueba que el correo tenga un formato basico valido antes de guardarlo.
    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str):
            raise DatosInvalidosError("El correo debe ser texto.")

        valor = valor.strip()

        patron = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(patron, valor):
            raise DatosInvalidosError("El correo electronico no tiene un formato válido.")

        self._correo = valor

# La propiedad permite consultar el teléfono
    @property
    def telefono(self):
        return self._telefono

# Convierte el teléfono a texto y comprueba que contenga entre 7 y 15 dígitos
    @telefono.setter
    def telefono(self, valor):
        texto = str(valor).strip()

        if not texto.isdigit() or not 7 <= len(texto) <= 15:
            raise DatosInvalidosError("El teléfono debe contener entre 7 y 15 dígitos.")

        self._telefono = texto

# Devuelve los datos principales del cliente en una sola cadena
    def mostrar_informacion(self):
        return (f"Cliente {self.identificador}: "f"{self.nombre} | {self.correo} | {self.telefono}")



