class SistemaFJError(Exception):
    """Excepción base del sistema Software FJ."""


class DatosInvalidosError(SistemaFJError):
    """Se usa cuando los datos ingresados no cumplen las reglas."""


class ElementoNoEncontradoError(SistemaFJError):
    """Se usa cuando no existe un cliente, servicio o reserva."""


class OperacionNoPermitidaError(SistemaFJError):
    """Se usa cuando una operación no está permitida."""
