from abc import abstractmethod
from entidades import Entidad
from excepciones import DatosInvalidosError


class Servicio(Entidad):
    """Clase abstracta que define el comportamiento común de un servicio."""

    def __init__(self, identificador, nombre, tarifa_base):
        super().__init__(identificador)
        if not nombre or not isinstance(nombre, str):
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")
        if not isinstance(tarifa_base, (int, float)) or tarifa_base <= 0:
            raise DatosInvalidosError("La tarifa base debe ser mayor que cero.")
        self.nombre = nombre.strip()
        self.tarifa_base = float(tarifa_base)

    @abstractmethod
    def calcular_costo(self, horas, descuento=0, impuesto=0):
        raise NotImplementedError

    @abstractmethod
    def validar_parametros(self, horas):
        raise NotImplementedError


class ReservaSala(Servicio):
    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise DatosInvalidosError("Las horas de sala deben ser mayores que cero.")

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        self.validar_parametros(horas)
        subtotal = self.tarifa_base * horas
        return subtotal * (1 - descuento) * (1 + impuesto)

    def mostrar_informacion(self):
        return f"Sala: {self.nombre} | tarifa/hora: ${self.tarifa_base:.2f}"


class AlquilerEquipo(Servicio):
    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise DatosInvalidosError("Las horas de alquiler deben ser mayores que cero.")

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        self.validar_parametros(horas)
        subtotal = self.tarifa_base * horas
        return subtotal * (1 - descuento) * (1 + impuesto)

    def mostrar_informacion(self):
        return f"Equipo: {self.nombre} | tarifa/hora: ${self.tarifa_base:.2f}"


class AsesoriaEspecializada(Servicio):
    def validar_parametros(self, horas):
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise DatosInvalidosError("La duración de la asesoría debe ser mayor que cero.")

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        self.validar_parametros(horas)
        subtotal = self.tarifa_base * horas
        return subtotal * (1 - descuento) * (1 + impuesto)

    def mostrar_informacion(self):
        return f"Asesoría: {self.nombre} | tarifa/hora: ${self.tarifa_base:.2f}"
