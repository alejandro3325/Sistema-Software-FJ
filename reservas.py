from entidades import Entidad
from excepciones import DatosInvalidosError, OperacionNoPermitidaError
from registro import registrar_evento


class Reserva(Entidad):
    """Relaciona un cliente con un servicio y controla su estado."""

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)
        if cliente is None or servicio is None:
            raise DatosInvalidosError("La reserva necesita un cliente y un servicio.")
        try:
            servicio.validar_parametros(duracion)
        except (TypeError, ValueError) as error:
            # Encadenamiento: conserva el error original como causa.
            raise DatosInvalidosError(
                "La duración de la reserva debe ser un número válido."
            ) from error
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado != "Pendiente":
            raise OperacionNoPermitidaError("Solo se puede confirmar una reserva pendiente.")
        self.estado = "Confirmada"
        registrar_evento(f"Reserva {self.identificador} confirmada.")

    def cancelar(self):
        if self.estado == "Cancelada":
            raise OperacionNoPermitidaError("La reserva ya está cancelada.")
        self.estado = "Cancelada"
        registrar_evento(f"Reserva {self.identificador} cancelada.")

    def procesar(self, descuento=0, impuesto=0):
        if self.estado != "Confirmada":
            raise OperacionNoPermitidaError("La reserva debe estar confirmada para procesarse.")
        if not 0 <= descuento < 1 or impuesto < 0:
            raise DatosInvalidosError("Descuento o impuesto fuera de rango.")
        return self.servicio.calcular_costo(self.duracion, descuento, impuesto)

    def mostrar_informacion(self):
        return (f"Reserva {self.identificador} | {self.cliente.nombre} | "
                f"{self.servicio.nombre} | {self.duracion} horas | {self.estado}")
