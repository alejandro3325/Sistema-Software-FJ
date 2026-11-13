"""Programa principal del sistema Software FJ."""

from clientes import Cliente
from servicios import (ReservaSala, AlquilerEquipo, AsesoriaEspecializada)
from reservas import Reserva
from excepciones import (SistemaFJError, ElementoNoEncontradoError)
from registro import registrar_evento, registrar_error

def ejecutar_operacion(descripcion, accion):
    """Ejecuta una operación controlando sus posibles errores."""

    print(f"\n{descripcion}")

    try:
        resultado = accion()

    except SistemaFJError as error:
        print(f"Error controlado: {error}")
        registrar_error(f"Error en operación: {descripcion}", error)

    except Exception as error:
        print(f"Error inesperado: {error}")
        registrar_error(f"Error inesperado en: {descripcion}", error)

    else:
        if resultado is not None:
            print(resultado)

        registrar_evento(f"Operación correcta: {descripcion}")

    finally:
        print("Operación finalizada.")


def obtener_elemento(lista, indice, descripcion):
    """Comprueba que exista un elemento antes de utilizarlo."""

    if len(lista) <= indice:
        raise ElementoNoEncontradoError(f"No existe el elemento requerido: {descripcion}.")

    return lista[indice]


def main():

    clientes = []
    servicios = []
    reservas = []

    # 1. Registro correcto de cliente.
    ejecutar_operacion("1. Registrar cliente válido", lambda: clientes.append(Cliente("C001", "Ana Pérez", "ana@email.com", "3001234567")))

    # 2. Intento de registro con correo inválido.
    ejecutar_operacion("2. Registrar cliente con correo inválido", lambda: clientes.append(Cliente("C002", "Luis Díaz", "correo-invalido","3101234567")))

    # 3. Segundo cliente válido.
    ejecutar_operacion("3. Registrar segundo cliente válido", lambda: clientes.append(Cliente("C003", "Carlos Ruiz", "carlos@email.com", "3201234567")))

    # 4. Crear servicio de reserva de sala.
    ejecutar_operacion("4. Crear servicio de reserva de sala", lambda: servicios.append(ReservaSala("S001", "Sala de reuniones", 50000)))

    # 5. Crear servicio de alquiler de equipo.
    ejecutar_operacion("5. Crear servicio de alquiler de equipo", lambda: servicios.append(AlquilerEquipo("S002", "Proyector", 25000)))

    # 6. Crear servicio de asesoría especializada.
    ejecutar_operacion("6. Crear servicio de asesoría especializada", lambda: servicios.append(AsesoriaEspecializada("S003","Asesoría Python", 70000)))

    # 7. Intentar crear un servicio con tarifa inválida.
    ejecutar_operacion("7. Crear servicio con tarifa inválida", lambda: servicios.append(ReservaSala("S004","Sala inválida",-1000)))

    # 8. Crear y confirmar una reserva válida.
    def crear_reserva():

        cliente = obtener_elemento(clientes, 0, "cliente C001")

        servicio = obtener_elemento(servicios, 0, "servicio S001")

        reserva = Reserva("R001", cliente, servicio,2)

        reserva.confirmar()
        reservas.append(reserva)

        return reserva.mostrar_informacion()

    ejecutar_operacion("8. Crear y confirmar reserva",crear_reserva)

    # 9. Procesar reserva confirmada con descuento e impuesto.
    def procesar_reserva():

        reserva = obtener_elemento(reservas, 0, "reserva R001")

        total = reserva.procesar(descuento=0.10, impuesto=0.19)

        return f"Costo total: ${total:,.2f}"

    ejecutar_operacion("9. Procesar reserva confirmada", procesar_reserva)

    # 10. Intentar procesar una reserva pendiente.
    def procesar_reserva_no_confirmada():

        cliente = obtener_elemento(clientes, 1, "cliente C003")

        servicio = obtener_elemento(servicios, 1, "servicio S002")

        reserva = Reserva("R002", cliente, servicio,3)

        reservas.append(reserva)

        return reserva.procesar()

    ejecutar_operacion("10. Procesar reserva pendiente (debe fallar)",procesar_reserva_no_confirmada)

    # Resumen del sistema.
    print("\n========== RESUMEN ==========")
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios registrados: {len(servicios)}")
    print(f"Reservas creadas: {len(reservas)}")

    print("\nConsulta logs.txt para revisar los eventos y errores.")
    print("El programa ha finalizado.")


if __name__ == "__main__":
    main()
