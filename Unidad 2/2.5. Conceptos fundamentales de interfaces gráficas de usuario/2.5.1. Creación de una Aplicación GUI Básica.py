# Importar la librería tkinter para crear la interfaz gráfica
import tkinter as tk
from tkinter import messagebox


# Crear la clase principal para nuestra aplicación
class GestorTareas:
    def __init__(self):
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("GESTOR DE TAREAS SARGENTO")
        self.ventana.geometry("600x500")

        # Lista para guardar las tareas
        self.lista_tareas = []

        # Crear los elementos de la interfaz
        self.crear_interfaz()

        # Iniciar el bucle principal
        self.ventana.mainloop()

    def crear_interfaz(self):
        # Sección superior - Entrada de tareas
        self.frame_superior = tk.Frame(self.ventana, bg="lightblue")
        self.frame_superior.pack(fill=tk.X, padx=10, pady=10)

        # Etiqueta para el campo de tarea
        self.label_tarea = tk.Label(self.frame_superior, text="Tarea:", bg="lightblue")
        self.label_tarea.grid(row=0, column=0, padx=5, pady=5)

        # Campo para escribir la tarea
        self.entrada_tarea = tk.Entry(self.frame_superior, width=30)
        self.entrada_tarea.grid(row=0, column=1, padx=5, pady=5)

        # Etiqueta para el campo de prioridad
        self.label_prioridad = tk.Label(self.frame_superior, text="Prioridad:", bg="lightblue")
        self.label_prioridad.grid(row=1, column=0, padx=5, pady=5)

        # Lista desplegable para la prioridad
        self.opciones_prioridad = ["Alta", "Media", "Baja"]
        self.variable_prioridad = tk.StringVar(self.ventana)
        self.variable_prioridad.set(self.opciones_prioridad[1])  # Valor por defecto

        self.menu_prioridad = tk.OptionMenu(self.frame_superior, self.variable_prioridad, *self.opciones_prioridad)
        self.menu_prioridad.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Botones
        self.boton_agregar = tk.Button(self.frame_superior, text="Agregar", command=self.agregar_tarea, bg="green",
                                       fg="white")
        self.boton_agregar.grid(row=2, column=0, padx=5, pady=5)

        self.boton_limpiar = tk.Button(self.frame_superior, text="Limpiar", command=self.limpiar_campos, bg="orange")
        self.boton_limpiar.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        # Sección central - Lista de tareas
        self.frame_central = tk.Frame(self.ventana)
        self.frame_central.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Título de la lista de tareas
        self.label_lista = tk.Label(self.frame_central, text="LISTA DE TAREAS:", font=("Arial", 12, "bold"))
        self.label_lista.pack(anchor="w")

        # Área para mostrar las tareas
        self.area_tareas = tk.Listbox(self.frame_central, width=50, height=10)
        self.area_tareas.pack(fill=tk.BOTH, expand=True)

        # Sección inferior - Botones adicionales
        self.frame_inferior = tk.Frame(self.ventana)
        self.frame_inferior.pack(fill=tk.X, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self.frame_inferior, text="Eliminar Seleccionada", command=self.eliminar_tarea,
                                        bg="red", fg="white")
        self.boton_eliminar.pack(side=tk.LEFT, padx=5)

    def agregar_tarea(self):
        # Obtener los valores de los campos
        texto_tarea = self.entrada_tarea.get()
        prioridad = self.variable_prioridad.get()

        # Verificar que se ingresó una tarea
        if texto_tarea == "":
            messagebox.showwarning("Alerta", "¡Debes escribir una tarea!")
            return

        # Crear el texto para mostrar en la lista
        tarea_completa = f"{texto_tarea} - Prioridad: {prioridad}"

        # Agregar la tarea a la lista y al listbox
        self.lista_tareas.append(tarea_completa)
        self.area_tareas.insert(tk.END, tarea_completa)

        # Limpiar el campo de entrada
        self.entrada_tarea.delete(0, tk.END)

        # Mostrar mensaje de confirmación
        messagebox.showinfo("Éxito", "¡Tarea agregada correctamente!")

    def limpiar_campos(self):
        # Borrar el texto del campo de entrada
        self.entrada_tarea.delete(0, tk.END)

        # Resetear la prioridad al valor por defecto
        self.variable_prioridad.set(self.opciones_prioridad[1])

    def eliminar_tarea(self):
        # Verificar si hay alguna tarea seleccionada
        try:
            # Obtener el índice seleccionado
            indice = self.area_tareas.curselection()[0]

            # Eliminar de la lista y del listbox
            self.lista_tareas.pop(indice)
            self.area_tareas.delete(indice)

            messagebox.showinfo("Éxito", "¡Tarea eliminada!")
        except:
            messagebox.showwarning("Error", "¡Debes seleccionar una tarea primero!")


# Crear una instancia de la aplicación
if __name__ == "__main__":
    app = GestorTareas()