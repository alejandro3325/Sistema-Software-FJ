
import math
from abc import abstractmethod

from entidades import Entidad
from excepciones import DatosInvalidosError


class Servicio(Entidad):
    """Clase abstracta que define el comportamiento de los servicios."""

    def __init__(self, identificador, nombre, tarifa_base):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del servicio es obligatorio."
            )

        if (
            isinstance(tarifa_base, bool)
            or not isinstance(tarifa_base, (int, float))
            or not math.isfinite(tarifa_base)
            or tarifa_base <= 0
        ):
            raise DatosInvalidosError(
                "La tarifa base debe ser un número mayor que cero."
            )

        self.nombre = nombre.strip()
        self.tarifa_base = float(tarifa_base)

    def _validar_calculo(self, horas, descuento, impuesto):
        """Valida los datos utilizados para calcular los costos."""

        self.validar_parametros(horas)

        for valor, nombre in (
            (descuento, "descuento"),
            (impuesto, "impuesto")
        ):
            if (
                isinstance(valor, bool)
                or not isinstance(valor, (int, float))
                or not math.isfinite(valor)
            ):
                raise DatosInvalidosError(
                    f"El {nombre} debe ser un número válido."
                )

        if not 0 <= descuento < 1:
            raise DatosInvalidosError(
                "El descuento debe estar entre 0 y menos del 100%."
            )

        if impuesto < 0:
            raise DatosInvalidosError(
                "El impuesto no puede ser negativo."
            )

    def _calcular_total(self, horas, descuento, impuesto):
        """Realiza el cálculo general del costo."""

        self._validar_calculo(horas, descuento, impuesto)

        subtotal = self.tarifa_base * horas
        total = subtotal * (1 - descuento) * (1 + impuesto)

        return total

    @abstractmethod
    def validar_parametros(self, horas):
        pass

    @abstractmethod
    def calcular_costo(self, horas, descuento=0, impuesto=0):
        pass


class ReservaSala(Servicio):

    def validar_parametros(self, horas):
        if (
            isinstance(horas, bool)
            or not isinstance(horas, (int, float))
            or not math.isfinite(horas)
            or horas <= 0
        ):
            raise DatosInvalidosError(
                "Las horas de sala deben ser mayores que cero."
            )

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        return self._calcular_total(horas, descuento, impuesto)

    def mostrar_informacion(self):
        return (
            f"Sala: {self.nombre} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f}"
        )


class AlquilerEquipo(Servicio):

    def validar_parametros(self, horas):
        if (
            isinstance(horas, bool)
            or not isinstance(horas, (int, float))
            or not math.isfinite(horas)
            or horas <= 0
        ):
            raise DatosInvalidosError(
                "Las horas de alquiler deben ser mayores que cero."
            )

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        return self._calcular_total(horas, descuento, impuesto)

    def mostrar_informacion(self):
        return (
            f"Equipo: {self.nombre} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f}"
        )


class AsesoriaEspecializada(Servicio):

    def validar_parametros(self, horas):
        if (
            isinstance(horas, bool)
            or not isinstance(horas, (int, float))
            or not math.isfinite(horas)
            or horas <= 0
        ):
            raise DatosInvalidosError(
                "La duración de la asesoría debe ser mayor que cero."
            )

    def calcular_costo(self, horas, descuento=0, impuesto=0):
        return self._calcular_total(horas, descuento, impuesto)

    def mostrar_informacion(self):
        return (
            f"Asesoría: {self.nombre} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f}"
        )

