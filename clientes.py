from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):
    """Representa a un cliente de Software FJ."""

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise DatosInvalidosError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor:
            raise DatosInvalidosError("El correo electrónico no es válido.")
        self._correo = valor.strip()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        texto = str(valor).strip()
        if not texto.isdigit() or len(texto) < 7:
            raise DatosInvalidosError("El teléfono debe contener al menos 7 dígitos.")
        self._telefono = texto

    def mostrar_informacion(self):
        return (f"Cliente {self.identificador}: {self.nombre} | "
                f"{self.correo} | {self.telefono}")
