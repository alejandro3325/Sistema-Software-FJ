# Interfaz gráfica de Software FJ desarrollada con Tkinter
# La interfaz utiliza las clases del proyecto; no reemplaza la lógica de negocio
# Tkinter crea la ventana y los controles; ttk aporta widgets con estilo y messagebox muestra avisos
import tkinter as tk
from tkinter import ttk, messagebox

# Importa las clases del proyecto que serán utilizadas desde los formularios
from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva
from excepciones import SistemaFJError
from registro import registrar_evento, registrar_error


# La clase reúne las pestañas, formularios, tablas y acciones de la aplicación
class AplicacionSoftwareFJ:
# Configura la ventana principal y prepara las listas donde se guardan los objetos
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Software FJ | Gestión integral")
        self.ventana.geometry("1050x680")
        self.ventana.minsize(900, 600)

        # Los datos se conservan en listas mientras la aplicación está abierta
        self.clientes = []
        self.servicios = []
        self.reservas = []

        self._crear_estilos()
        self._crear_interfaz()
        self._actualizar_todo()

# Define estilos visuales para títulos, tablas y botones
    def _crear_estilos(self):
        estilo = ttk.Style()
        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass
        estilo.configure("Titulo.TLabel", font=("Segoe UI", 19, "bold"))
        estilo.configure("Subtitulo.TLabel", font=("Segoe UI", 10))
        estilo.configure("Treeview", rowheight=27, font=("Segoe UI", 9))
        estilo.configure("Treeview.Heading", font=("Segoe UI", 9, "bold"))
        estilo.configure("Accion.TButton", padding=7)

# Construye el encabezado, el resumen y las pestañas principales
    def _crear_interfaz(self):
        encabezado = ttk.Frame(self.ventana, padding=(18, 14))
        encabezado.pack(fill="x")
        ttk.Label(encabezado, text="Software FJ", style="Titulo.TLabel").pack(anchor="w")
        ttk.Label(encabezado, text="Sistema integral de clientes, servicios y reservas", style="Subtitulo.TLabel").pack(anchor="w")

        self.resumen = ttk.Label(self.ventana, text="", padding=(18, 4))
        self.resumen.pack(fill="x")

        self.pestanas = ttk.Notebook(self.ventana)
        self.pestanas.pack(fill="both", expand=True, padx=16, pady=12)
        self.tab_clientes = ttk.Frame(self.pestanas, padding=12)
        self.tab_servicios = ttk.Frame(self.pestanas, padding=12)
        self.tab_reservas = ttk.Frame(self.pestanas, padding=12)
        self.tab_registros = ttk.Frame(self.pestanas, padding=12)
        self.pestanas.add(self.tab_clientes, text="Clientes")
        self.pestanas.add(self.tab_servicios, text="Servicios")
        self.pestanas.add(self.tab_reservas, text="Reservas")
        self.pestanas.add(self.tab_registros, text="Registros")

        self._crear_tab_clientes()
        self._crear_tab_servicios()
        self._crear_tab_reservas()
        self._crear_tab_registros()

# Crea una etiqueta y una caja de texto para capturar un dato
    def _campo(self, padre, etiqueta, fila, columna, ancho=24):
        ttk.Label(padre, text=etiqueta).grid(row=fila, column=columna, sticky="w", padx=5, pady=5)
        entrada = ttk.Entry(padre, width=ancho)
        entrada.grid(row=fila + 1, column=columna, sticky="ew", padx=5, pady=(0, 8))
        return entrada

# Crea una tabla con encabezados y una barra de desplazamiento vertical
    def _tabla(self, padre, columnas, encabezados):
        contenedor = ttk.Frame(padre)
        contenedor.pack(fill="both", expand=True, pady=(12, 4))
        tabla = ttk.Treeview(contenedor, columns=columnas, show="headings", height=12)
        for columna, titulo in zip(columnas, encabezados):
            tabla.heading(columna, text=titulo)
            tabla.column(columna, width=145, anchor="w")
        barra = ttk.Scrollbar(contenedor, orient="vertical", command=tabla.yview)
        tabla.configure(yscrollcommand=barra.set)
        tabla.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")
        return tabla

# Construye el formulario y la tabla para registrar y consultar clientes
    def _crear_tab_clientes(self):
        formulario = ttk.LabelFrame(self.tab_clientes, text="Registrar cliente", padding=10)
        formulario.pack(fill="x")
        for columna in range(4):
            formulario.columnconfigure(columna, weight=1)
        self.cli_id = self._campo(formulario, "Identificador", 0, 0)
        self.cli_nombre = self._campo(formulario, "Nombre", 0, 1)
        self.cli_correo = self._campo(formulario, "Correo", 0, 2)
        self.cli_telefono = self._campo(formulario, "Teléfono", 0, 3)
        ttk.Button(formulario, text="Registrar cliente", style="Accion.TButton", command=self.registrar_cliente).grid(row=2, column=0, columnspan=4, sticky="ew", padx=5)
        self.tabla_clientes = self._tabla(self.tab_clientes, ("id", "nombre", "correo", "telefono"), ("ID", "Nombre", "Correo", "Teléfono"))

# Construye los controles para crear servicios de los tres tipos disponibles
    def _crear_tab_servicios(self):
        formulario = ttk.LabelFrame(self.tab_servicios, text="Crear servicio", padding=10)
        formulario.pack(fill="x")
        for columna in range(3):
            formulario.columnconfigure(columna, weight=1)
        self.ser_tipo = tk.StringVar(value="Reserva de sala")
        ttk.Label(formulario, text="Tipo de servicio").grid(row=0, column=0, sticky="w", padx=5)
        ttk.Combobox(formulario, textvariable=self.ser_tipo, state="readonly", values=("Reserva de sala", "Alquiler de equipo", "Asesoría especializada")).grid(row=1, column=0, sticky="ew", padx=5, pady=(0, 8))
        self.ser_nombre = self._campo(formulario, "Nombre del servicio", 0, 1)
        self.ser_tarifa = self._campo(formulario, "Tarifa por hora (COP)", 0, 2)
        ttk.Button(formulario, text="Crear servicio", style="Accion.TButton", command=self.crear_servicio).grid(row=2, column=0, columnspan=3, sticky="ew", padx=5)
        self.tabla_servicios = self._tabla(self.tab_servicios, ("id", "tipo", "nombre", "tarifa"), ("ID", "Tipo", "Nombre", "Tarifa por hora"))

# Construye el formulario de reservas y los botones para cambiar su estado
    def _crear_tab_reservas(self):
        formulario = ttk.LabelFrame(self.tab_reservas, text="Nueva reserva", padding=10)
        formulario.pack(fill="x")
        formulario.columnconfigure(0, weight=1)
        formulario.columnconfigure(1, weight=1)
        formulario.columnconfigure(2, weight=1)
        self.res_cliente = tk.StringVar()
        self.res_servicio = tk.StringVar()
        ttk.Label(formulario, text="Cliente").grid(row=0, column=0, sticky="w", padx=5)
        self.combo_cliente = ttk.Combobox(formulario, textvariable=self.res_cliente, state="readonly")
        self.combo_cliente.grid(row=1, column=0, sticky="ew", padx=5, pady=(0, 8))
        ttk.Label(formulario, text="Servicio").grid(row=0, column=1, sticky="w", padx=5)
        self.combo_servicio = ttk.Combobox(formulario, textvariable=self.res_servicio, state="readonly")
        self.combo_servicio.grid(row=1, column=1, sticky="ew", padx=5, pady=(0, 8))
        self.res_duracion = self._campo(formulario, "Duración (horas)", 0, 2)
        ttk.Button(formulario, text="Crear reserva", command=self.crear_reserva).grid(row=2, column=0, columnspan=3, sticky="ew", padx=5)

        acciones = ttk.Frame(self.tab_reservas)
        acciones.pack(fill="x", pady=(10, 0))
        ttk.Button(acciones, text="Confirmar", command=self.confirmar_reserva).pack(side="left", padx=(0, 6))
        ttk.Button(acciones, text="Cancelar", command=self.cancelar_reserva).pack(side="left", padx=6)
        ttk.Button(acciones, text="Procesar", command=self.procesar_reserva).pack(side="left", padx=6)
        self.tabla_reservas = self._tabla(self.tab_reservas, ("id", "cliente", "servicio", "duracion", "estado"), ("ID", "Cliente", "Servicio", "Duración", "Estado"))
        ttk.Label(self.tab_reservas, text="Selecciona una reserva de la tabla antes de confirmar, cancelar o procesar.").pack(anchor="w", pady=4)

# Muestra el contenido del archivo de eventos y errores
    def _crear_tab_registros(self):
        ttk.Label(self.tab_registros, text="Eventos y errores guardados en logs.txt").pack(anchor="w")
        self.texto_logs = tk.Text(self.tab_registros, height=22, wrap="word", state="disabled")
        self.texto_logs.pack(fill="both", expand=True, pady=8)
        ttk.Button(self.tab_registros, text="Actualizar registros", command=self.actualizar_logs).pack(anchor="e")

# Ejecuta una acción, captura errores, muestra avisos y actualiza la interfaz
    def _ejecutar(self, descripcion, accion):
        try:
            resultado = accion()
        except SistemaFJError as error:
            registrar_error(f"{descripcion}", error)
            messagebox.showerror("No se pudo completar", str(error))
            self.actualizar_logs()
            return None
        except (ValueError, TypeError) as error:
            registrar_error(f"{descripcion}", error)
            messagebox.showerror("Dato inválido", str(error))
            self.actualizar_logs()
            return None
        except Exception as error:
            registrar_error(f"Error inesperado: {descripcion}", error)
            messagebox.showerror("Error inesperado", "Ocurrió un problema. Revisa logs.txt para más información.")
            self.actualizar_logs()
            return None
        else:
            registrar_evento(descripcion)
            self._actualizar_todo()
            self.actualizar_logs()
            return resultado
        finally:
            pass

# Valida y registra un cliente a partir de los campos del formulario
    def registrar_cliente(self):
        def accion():
            identificador = self.cli_id.get().strip()
            if any(c.identificador == identificador for c in self.clientes):
                raise ValueError("Ya existe un cliente con ese identificador.")
            cliente = Cliente(identificador, self.cli_nombre.get(), self.cli_correo.get(), self.cli_telefono.get())
            self.clientes.append(cliente)
            for campo in (self.cli_id, self.cli_nombre, self.cli_correo, self.cli_telefono):
                campo.delete(0, tk.END)
            return cliente
        self._ejecutar("Registro de cliente desde la interfaz", accion)

# Identifica el tipo de servicio elegido, crea el objeto y lo agrega a la lista
    def crear_servicio(self):
        def accion():
            tarifa = float(self.ser_tarifa.get().strip())
            identificador = f"S{len(self.servicios) + 1:03d}"
            clases = {"Reserva de sala": ReservaSala, "Alquiler de equipo": AlquilerEquipo, "Asesoría especializada": AsesoriaEspecializada}
            clase = clases[self.ser_tipo.get()]
            servicio = clase(identificador, self.ser_nombre.get(), tarifa)
            self.servicios.append(servicio)
            self.ser_nombre.delete(0, tk.END)
            self.ser_tarifa.delete(0, tk.END)
            return servicio
        self._ejecutar("Creación de servicio desde la interfaz", accion)

# Busca el cliente y el servicio seleccionados y crea una nueva reserva
    def crear_reserva(self):
        def accion():
            cliente_id = self.res_cliente.get().split(" | ")[0]
            servicio_id = self.res_servicio.get().split(" | ")[0]
            cliente = next((c for c in self.clientes if c.identificador == cliente_id), None)
            servicio = next((s for s in self.servicios if s.identificador == servicio_id), None)
            if cliente is None or servicio is None:
                raise ValueError("Debes seleccionar un cliente y un servicio existentes.")
            duracion = float(self.res_duracion.get().strip())
            identificador = f"R{len(self.reservas) + 1:03d}"
            reserva = Reserva(identificador, cliente, servicio, duracion)
            self.reservas.append(reserva)
            self.res_duracion.delete(0, tk.END)
            return reserva
        self._ejecutar("Creación de reserva desde la interfaz", accion)

# Obtiene la reserva marcada en la tabla; si no hay selección, informa el problema
    def _reserva_seleccionada(self):
        seleccion = self.tabla_reservas.selection()
        if not seleccion:
            raise ValueError("Selecciona una reserva de la tabla.")
        identificador = self.tabla_reservas.item(seleccion[0], "values")[0]
        return next(r for r in self.reservas if r.identificador == identificador)

# Confirma la reserva seleccionada
    def confirmar_reserva(self):
        self._ejecutar("Confirmación de reserva", lambda: self._reserva_seleccionada().confirmar())

# Cancela la reserva seleccionada
    def cancelar_reserva(self):
        self._ejecutar("Cancelación de reserva", lambda: self._reserva_seleccionada().cancelar())

# Calcula el costo de una reserva confirmada y muestra el total
    def procesar_reserva(self):
        def accion():
            reserva = self._reserva_seleccionada()
            total = reserva.procesar()
            messagebox.showinfo("Reserva procesada", f"Total a pagar: ${total:,.0f} COP")
            return total
        self._ejecutar("Procesamiento de reserva", accion)

# Actualiza las tablas, el resumen y las opciones de los menús desplegables
    def _actualizar_todo(self):
        self._llenar(self.tabla_clientes, [(c.identificador, c.nombre, c.correo, c.telefono) for c in self.clientes])
        filas_servicios = []
        for s in self.servicios:
            tipo = type(s).__name__
            filas_servicios.append((s.identificador, tipo, s.nombre, f"${s.tarifa_base:,.0f}"))
        self._llenar(self.tabla_servicios, filas_servicios)
        self._llenar(self.tabla_reservas, [(r.identificador, r.cliente.nombre, r.servicio.nombre, r.duracion, r.estado) for r in self.reservas])
        self.resumen.config(text=f"Clientes: {len(self.clientes)}     Servicios: {len(self.servicios)}     Reservas: {len(self.reservas)}")
        if hasattr(self, "combo_cliente"):
            self.combo_cliente["values"] = [f"{c.identificador} | {c.nombre}" for c in self.clientes]
            self.combo_servicio["values"] = [f"{s.identificador} | {s.nombre}" for s in self.servicios]

# Elimina las filas actuales de una tabla y agrega las filas actualizadas
    @staticmethod
    def _llenar(tabla, filas):
        for elemento in tabla.get_children():
            tabla.delete(elemento)
        for fila in filas:
            tabla.insert("", "end", values=fila)

# Lee logs.txt y muestra su contenido en el área de texto de la pestaña Registros
    def actualizar_logs(self):
        try:
            with open("logs.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()
        except FileNotFoundError:
            contenido = "Todavía no se ha generado el archivo de registros."
        self.texto_logs.config(state="normal")
        self.texto_logs.delete("1.0", tk.END)
        self.texto_logs.insert("1.0", contenido)
        self.texto_logs.config(state="disabled")


# Crea la ventana, instancia la aplicación y mantiene abierta la interfaz
def iniciar_aplicacion():
    ventana = tk.Tk()
    AplicacionSoftwareFJ(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    iniciar_aplicacion()
