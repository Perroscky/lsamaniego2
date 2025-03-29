# GESTOR DE TAREAS ACTUALIZADO

import tkinter as tk
from tkinter import ttk, messagebox
import pickle
import os


class GestorTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Comando-Paraca")
        self.root.geometry("500x500")
        self.root.config(bg="#000000")  # Fondo negro

        # Archivo para guardar las tareas
        self.archivo_tareas = "tareas.dat"

        # Lista para almacenar tareas
        self.tareas = []

        # Cargar tareas anteriores si existen
        self.cargar_tareas()

        # Configurar la interfaz
        self.configurar_interfaz()

        # Configurar atajos de teclado
        self.configurar_atajos()

    def configurar_interfaz(self):
        """Configura todos los elementos de la interfaz gráfica"""
        # Frame principal
        frame_principal = tk.Frame(self.root, bg="#000000")  # Fondo negro
        frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Título
        titulo = tk.Label(frame_principal, text="Gestor de Tareas Comando-Paraca", font=("Arial", 16, "bold"),
                          bg="#000000", fg="#FFFF00")  # Texto amarillo sobre fondo negro
        titulo.pack(pady=10)

        # Frame para entrada y botón de añadir
        frame_entrada = tk.Frame(frame_principal, bg="#000000")  # Fondo negro
        frame_entrada.pack(fill=tk.X, pady=10)

        # Entrada para nuevas tareas
        self.entrada_tarea = tk.Entry(frame_entrada, font=("Arial", 12), width=30, bg="#FFFFDD")  # Fondo amarillo claro
        self.entrada_tarea.pack(side=tk.LEFT, padx=(0, 10), ipady=3)
        self.entrada_tarea.focus_set()  # Poner el foco en la entrada

        # Botón para añadir tareas
        self.boton_añadir = tk.Button(frame_entrada, text="Añadir", command=self.añadir_tarea,
                                      bg="#00AA00", fg="#FFFFFF", font=("Arial", 10, "bold"), padx=10)  # Verde
        self.boton_añadir.pack(side=tk.LEFT)

        # Frame para la lista de tareas y barra de desplazamiento
        frame_lista = tk.Frame(frame_principal, bg="#000000")  # Fondo negro
        frame_lista.pack(fill=tk.BOTH, expand=True, pady=10)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configurar estilo para Treeview
        style = ttk.Style()
        style.configure("Treeview",
                        background="#000000",  # Fondo negro
                        foreground="#FFFFFF",  # Texto blanco
                        fieldbackground="#000000",  # Fondo del campo negro
                        font=("Arial", 11),
                        rowheight=30)

        style.configure("Treeview.Heading",
                        background="#00AA00",  # Fondo verde para cabeceras
                        foreground="#FFFFFF",  # Texto blanco
                        font=("Arial", 11, "bold"))

        # Lista de tareas usando Treeview para mejor presentación
        self.lista_tareas = ttk.Treeview(frame_lista, columns=("estado",),
                                         show="tree headings", selectmode="browse",
                                         yscrollcommand=scrollbar.set,
                                         style="Treeview")
        self.lista_tareas.heading("#0", text="Tarea")
        self.lista_tareas.heading("estado", text="Estado")
        self.lista_tareas.column("#0", width=380, minwidth=200)
        self.lista_tareas.column("estado", width=100, minwidth=80, anchor="center")
        self.lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.lista_tareas.yview)

        # Frame para botones
        frame_botones = tk.Frame(frame_principal, bg="#000000")  # Fondo negro
        frame_botones.pack(fill=tk.X, pady=10)

        # Botón para marcar como completada
        self.boton_completar = tk.Button(frame_botones, text="Completar (C)", command=self.completar_tarea,
                                         bg="#00AA00", fg="#FFFFFF", font=("Arial", 10, "bold"), padx=10)  # Verde
        self.boton_completar.pack(side=tk.LEFT, padx=(0, 10))

        # Botón para eliminar
        self.boton_eliminar = tk.Button(frame_botones, text="Eliminar (D)", command=self.eliminar_tarea,
                                        bg="#FFFF00", fg="#000000", font=("Arial", 10, "bold"), padx=10)  # Amarillo
        self.boton_eliminar.pack(side=tk.LEFT)

        # Etiqueta para atajos
        tk.Label(frame_principal, text="Atajos: Enter para añadir, C para completar, D para eliminar, Esc para salir",
                 font=("Arial", 9), bg="#000000", fg="#FFFF00").pack(side=tk.BOTTOM, pady=5)  # Texto amarillo

        # Cargar tareas existentes en la lista
        self.actualizar_lista_tareas()

    def configurar_atajos(self):
        """Configura los atajos de teclado"""
        # Enter para añadir tarea
        self.entrada_tarea.bind("<Return>", lambda event: self.añadir_tarea())

        # C para completar tarea seleccionada
        self.root.bind("<c>", lambda event: self.completar_tarea())
        self.root.bind("<C>", lambda event: self.completar_tarea())

        # D para eliminar tarea seleccionada
        self.root.bind("<d>", lambda event: self.eliminar_tarea())
        self.root.bind("<D>", lambda event: self.eliminar_tarea())
        self.root.bind("<Delete>", lambda event: self.eliminar_tarea())

        # Escape para cerrar la aplicación
        self.root.bind("<Escape>", lambda event: self.salir())

    def añadir_tarea(self):
        """Añade una nueva tarea a la lista"""
        texto = self.entrada_tarea.get().strip()
        if texto:
            # Crear objeto de tarea
            tarea = {
                "texto": texto,
                "completada": False
            }
            # Añadir a la lista de tareas
            self.tareas.append(tarea)
            # Guardar en archivo
            self.guardar_tareas()
            # Actualizar la lista visual
            self.actualizar_lista_tareas()
            # Limpiar el campo de entrada
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea.")
        # Devolver el foco a la entrada
        self.entrada_tarea.focus_set()

    def completar_tarea(self):
        """Marca como completada la tarea seleccionada"""
        seleccion = self.lista_tareas.selection()
        if seleccion:
            indice = self.lista_tareas.index(seleccion[0])
            # Alternar estado
            self.tareas[indice]["completada"] = not self.tareas[indice]["completada"]
            # Guardar cambios
            self.guardar_tareas()
            # Actualizar lista
            self.actualizar_lista_tareas()
        else:
            messagebox.showinfo("Selección", "Por favor, selecciona una tarea.")

    def eliminar_tarea(self):
        """Elimina la tarea seleccionada"""
        seleccion = self.lista_tareas.selection()
        if seleccion:
            indice = self.lista_tareas.index(seleccion[0])
            # Eliminar tarea
            del self.tareas[indice]
            # Guardar cambios
            self.guardar_tareas()
            # Actualizar lista
            self.actualizar_lista_tareas()
        else:
            messagebox.showinfo("Selección", "Por favor, selecciona una tarea.")

    def actualizar_lista_tareas(self):
        """Actualiza la visualización de la lista de tareas"""
        # Limpiar lista actual
        for item in self.lista_tareas.get_children():
            self.lista_tareas.delete(item)

        # Añadir todas las tareas
        for tarea in self.tareas:
            estado = "Completada" if tarea["completada"] else "Pendiente"

            # Insertar con formato según estado
            item = self.lista_tareas.insert("", "end", text=tarea["texto"], values=(estado,))

            # Cambiar color según estado
            if tarea["completada"]:
                self.lista_tareas.item(item, tags=("completada",))

        # Configurar etiquetas de estilo
        self.lista_tareas.tag_configure("completada", foreground="#FFFF00")  # Amarillo para tareas completadas

    def cargar_tareas(self):
        """Carga las tareas desde un archivo .dat usando pickle"""
        try:
            if os.path.exists(self.archivo_tareas):
                with open(self.archivo_tareas, "rb") as archivo:
                    self.tareas = pickle.load(archivo)
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar las tareas: {str(e)}")
            self.tareas = []

    def guardar_tareas(self):
        """Guarda las tareas en un archivo .dat usando pickle"""
        try:
            with open(self.archivo_tareas, "wb") as archivo:
                pickle.dump(self.tareas, archivo)
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar las tareas: {str(e)}")

    def salir(self):
        """Cierra la aplicación"""
        if messagebox.askokcancel("Salir", "¿Deseas cerrar la aplicación?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = GestorTareas(root)
    root.protocol("WM_DELETE_WINDOW", app.salir)  # Manejar cierre de ventana
    root.mainloop()