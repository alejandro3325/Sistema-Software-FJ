# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

Proyecto académico en Python para gestionar clientes, servicios y reservas sin utilizar bases de datos.

## Requisitos
- Python 3.9 o superior.
- No requiere instalar paquetes externos.

## Archivos
- `entidades.py`: clase abstracta general.
- `clientes.py`: clase Cliente y validaciones.
- `servicios.py`: clase abstracta Servicio y tres servicios especializados.
- `reservas.py`: creación, confirmación, cancelación y procesamiento de reservas.
- `excepciones.py`: excepciones personalizadas.
- `registro.py`: registro de eventos y errores en `logs.txt`.
- `main.py`: demostración de diez operaciones.
- `logs.txt`: se genera automáticamente al ejecutar el programa y guarda eventos y errores.

El cálculo de costos admite variantes mediante parámetros opcionales (horas, descuento e impuesto). También se incluye encadenamiento de excepciones con `raise ... from ...`, además de bloques `try/except/else/finally`.

## Ejecución
Desde esta carpeta, ejecutar:

```bash
python main.py
```

El archivo `logs.txt` se crea automáticamente al ejecutar el programa.

## Nota de trabajo colaborativo
Esta es una base inicial. El grupo debe revisar, ejecutar, probar y adaptar el proyecto conjuntamente, distribuir responsabilidades y documentar los aportes de cada integrante.
