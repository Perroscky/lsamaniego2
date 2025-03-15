import tkinter as tk
from tkinter import ttk, messagebox
import pickle
from tkcalendar import DateEntry
from datetime import datetime


class AgendaPersonal:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Agenda Personal Sargento")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        # Variables para almacenar los datos de entrada
        self.fecha_var = tk.StringVar()
        self.hora_var = tk.StringVar()
        self.descripcion_var = tk.StringVar()

        # Lista para almacenar eventos
        self.eventos = []

        # Cargar eventos guardados (si existen)
        self.cargar_eventos()

        # Crear los frames principales
        self.crear_frames()

        # Inicializar componentes de la interfaz
        self.crear_componentes_entrada()
        self.crear_tabla_eventos()
        self.crear_botones()

    def crear_frames(self):
        # Frame superior para entrada de datos
        self.frame_entrada = tk.Frame(self.root, bg="black", padx=10, pady=10)
        self.frame_entrada.pack(fill="x", padx=10, pady=10)

        # Frame medio para la tabla de eventos
        self.frame_tabla = tk.Frame(self.root, bg="black", padx=10, pady=10)
        self.frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame inferior para botones
        self.frame_botones = tk.Frame(self.root, bg="black", padx=10, pady=10)
        self.frame_botones.pack(fill="x", padx=10, pady=10)

    def crear_componentes_entrada(self):
        # Etiqueta y selector de fecha
        tk.Label(self.frame_entrada, text="Fecha:", bg="black", fg="yellow", font=("Arial", 12)).grid(row=0, column=0,
                                                                                                      padx=5, pady=5,
                                                                                                      sticky="w")
        self.date_picker = DateEntry(self.frame_entrada, width=12, background="green", foreground="white",
                                     borderwidth=2, date_pattern="dd/mm/yyyy")
        self.date_picker.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Etiqueta y entrada para hora
        tk.Label(self.frame_entrada, text="Hora (HH:MM):", bg="black", fg="yellow", font=("Arial", 12)).grid(row=0,
                                                                                                             column=2,
                                                                                                             padx=5,
                                                                                                             pady=5,
                                                                                                             sticky="w")
        hora_entry = tk.Entry(self.frame_entrada, textvariable=self.hora_var, width=10, bg="green", fg="white",
                              insertbackground="white")
        hora_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        # Etiqueta y entrada para descripción
        tk.Label(self.frame_entrada, text="Descripción:", bg="black", fg="yellow", font=("Arial", 12)).grid(row=1,
                                                                                                            column=0,
                                                                                                            padx=5,
                                                                                                            pady=5,
                                                                                                            sticky="w")
        descripcion_entry = tk.Entry(self.frame_entrada, textvariable=self.descripcion_var, width=50, bg="green",
                                     fg="white", insertbackground="white")
        descripcion_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="we")

    def crear_tabla_eventos(self):
        # Crear un Treeview para mostrar los eventos
        columnas = ("fecha", "hora", "descripcion")
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")

        # Definir los encabezados de las columnas
        self.tabla.heading("fecha", text="Fecha")
        self.tabla.heading("hora", text="Hora")
        self.tabla.heading("descripcion", text="Descripción")

        # Configurar el ancho de las columnas
        self.tabla.column("fecha", width=100)
        self.tabla.column("hora", width=100)
        self.tabla.column("descripcion", width=500)

        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        # Colocar el Treeview y la scrollbar en el frame
        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Estilo personalizado para el Treeview
        estilo = ttk.Style()
        estilo.configure("Treeview",
                         background="black",
                         foreground="green",
                         rowheight=25,
                         fieldbackground="black")
        estilo.map('Treeview', background=[('selected', 'green')])
        estilo.configure("Treeview.Heading",
                         background="yellow",
                         foreground="black",
                         relief="flat")

        # Cargar eventos en la tabla
        self.actualizar_tabla()

    def crear_botones(self):
        # Botón para agregar evento
        self.btn_agregar = tk.Button(
            self.frame_botones,
            text="Agregar Evento",
            command=self.agregar_evento,
            bg="green",
            fg="white",
            activebackground="yellow",
            activeforeground="black",
            font=("Arial", 11, "bold"),
            width=15,
            height=2
        )
        self.btn_agregar.pack(side="left", padx=10)

        # Botón para eliminar evento seleccionado
        self.btn_eliminar = tk.Button(
            self.frame_botones,
            text="Eliminar Evento",
            command=self.eliminar_evento,
            bg="green",
            fg="white",
            activebackground="yellow",
            activeforeground="black",
            font=("Arial", 11, "bold"),
            width=15,
            height=2
        )
        self.btn_eliminar.pack(side="left", padx=10)

        # Botón para salir
        self.btn_salir = tk.Button(
            self.frame_botones,
            text="Salir",
            command=self.root.destroy,
            bg="yellow",
            fg="black",
            activebackground="green",
            activeforeground="white",
            font=("Arial", 11, "bold"),
            width=15,
            height=2
        )
        self.btn_salir.pack(side="right", padx=10)

    def agregar_evento(self):
        # Obtener datos de los campos de entrada
        fecha = self.date_picker.get_date().strftime("%d/%m/%Y")
        hora = self.hora_var.get()
        descripcion = self.descripcion_var.get()

        # Validar que se hayan ingresado todos los datos
        if not hora or not descripcion:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        # Validar formato de hora (HH:MM)
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "El formato de hora debe ser HH:MM (ejemplo: 14:30)")
            return

        # Crear un nuevo evento y agregarlo a la lista
        nuevo_evento = {
            "fecha": fecha,
            "hora": hora,
            "descripcion": descripcion
        }

        self.eventos.append(nuevo_evento)

        # Actualizar la tabla y guardar eventos
        self.actualizar_tabla()
        self.guardar_eventos()

        # Limpiar campos de entrada
        self.hora_var.set("")
        self.descripcion_var.set("")

        messagebox.showinfo("Éxito", "Evento agregado correctamente.")

    def eliminar_evento(self):
        # Obtener el ítem seleccionado
        seleccion = self.tabla.selection()

        if not seleccion:
            messagebox.showerror("Error", "Por favor seleccione un evento para eliminar.")
            return

        # Confirmar eliminación
        confirmacion = messagebox.askyesno("Confirmar eliminación", "¿Está seguro que desea eliminar este evento?")

        if confirmacion:
            # Obtener el índice del evento seleccionado
            indice = self.tabla.index(seleccion[0])

            # Eliminar el evento de la lista
            del self.eventos[indice]

            # Actualizar la tabla y guardar eventos
            self.actualizar_tabla()
            self.guardar_eventos()

            messagebox.showinfo("Éxito", "Evento eliminado correctamente.")

    def actualizar_tabla(self):
        # Limpiar la tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Ordenar eventos por fecha y hora
        eventos_ordenados = sorted(
            self.eventos,
            key=lambda x: (
                datetime.strptime(x["fecha"], "%d/%m/%Y"),
                datetime.strptime(x["hora"], "%H:%M")
            )
        )

        # Insertar eventos en la tabla
        for evento in eventos_ordenados:
            self.tabla.insert("", "end", values=(evento["fecha"], evento["hora"], evento["descripcion"]))

    def guardar_eventos(self):
        # Guardar eventos en un archivo .dat
        try:
            with open("agenda_eventos.dat", "wb") as archivo:
                pickle.dump(self.eventos, archivo)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los eventos: {str(e)}")

    def cargar_eventos(self):
        # Cargar eventos desde un archivo .dat (si existe)
        try:
            with open("agenda_eventos.dat", "rb") as archivo:
                self.eventos = pickle.load(archivo)
        except FileNotFoundError:
            self.eventos = []  # Si el archivo no existe, iniciar con lista vacía
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los eventos: {str(e)}")
            self.eventos = []


# Función principal para iniciar la aplicación
def main():
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()


if __name__ == "__main__":
    main()