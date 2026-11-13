import math

from entidades import Entidad
from clientes import Cliente
from servicios import Servicio
from excepciones import (DatosInvalidosError, OperacionNoPermitidaError)
from registro import registrar_evento

class Reserva(Entidad):
    """Relaciona un cliente con un servicio y controla su estado."""

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)

        if not isinstance(cliente, Cliente):
            raise DatosInvalidosError(
                "Debe proporcionar un cliente válido."
            )

        if not isinstance(servicio, Servicio):
            raise DatosInvalidosError(
                "Debe proporcionar un servicio válido."
            )

        try:
            servicio.validar_parametros(duracion)

        except (TypeError, ValueError, DatosInvalidosError) as error:
            raise DatosInvalidosError(
                "La duración de la reserva debe ser un número válido y positivo."
            ) from error

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

        registrar_evento(
            f"Reserva {self.identificador} creada."
        )

    def confirmar(self):
        if self.estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se puede confirmar una reserva pendiente."
            )

        self.estado = "Confirmada"

        registrar_evento(
            f"Reserva {self.identificador} confirmada."
        )

    def cancelar(self):
        if self.estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya está cancelada."
            )

        self.estado = "Cancelada"

        registrar_evento(
            f"Reserva {self.identificador} cancelada."
        )

    def procesar(self, descuento=0, impuesto=0):
        if self.estado != "Confirmada":
            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada para procesarse."
            )

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

        if not 0 <= descuento < 1 or impuesto < 0:
            raise DatosInvalidosError(
                "El descuento o el impuesto están fuera de rango."
            )

        total = self.servicio.calcular_costo(
            self.duracion,
            descuento,
            impuesto
        )

        registrar_evento(
            f"Reserva {self.identificador} procesada. "
            f"Total: ${total:.2f}"
        )

        return total

    def mostrar_informacion(self):
        return (
            f"Reserva {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Duración: {self.duracion} horas | "
            f"Estado: {self.estado}"
        )

