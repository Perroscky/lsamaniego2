# Aplicación GUI de Lista de Tareas El Sargento

import tkinter as tk
from tkinter import messagebox, ttk
import pickle
import os


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("El Sargento - Gestor de Tareas Militar")
        self.root.geometry("550x450")

        # Nueva paleta de colores
        self.bg_color = "#0F1A0E"  # Verde oscuro
        self.button_color = "#FFD700"  # Amarillo oro
        self.button_text_color = "#000000"  # Negro para contraste
        self.text_color = "#FFFF00"  # Amarillo
        self.completed_bg = "#2A3010"  # Verde militar oscuro

        self.root.configure(bg=self.bg_color)

        self.data_file = "tareas_sargento.dat"
        self.tareas = self.cargar_tareas()

        self.configurar_estilo()
        self.crear_interfaz()
        self.configurar_eventos()
        self.actualizar_lista()

    def configurar_estilo(self):
        style = ttk.Style()
        style.configure("TFrame", background=self.bg_color)
        style.configure("TLabel", background=self.bg_color, foreground=self.text_color, font=("Arial", 10, "bold"))
        style.configure("Title.TLabel", background=self.bg_color, foreground=self.text_color,
                        font=("Arial", 14, "bold"))
        style.configure("TButton", background=self.button_color, foreground=self.button_text_color,
                        font=("Arial", 10, "bold"))
        style.map("TButton", background=[("active", "#E6C200")])

    def crear_interfaz(self):
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(main_frame, text="LISTA DE TAREAS EL SARGENTO", style="Title.TLabel").pack(pady=(0, 15))

        ttk.Label(main_frame, text="Nueva Misión:").pack(anchor=tk.W)
        self.entrada_tarea = ttk.Entry(main_frame, width=50)
        self.entrada_tarea.pack(fill=tk.X, pady=8)

        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=10)

        ttk.Button(btn_frame, text="AÑADIR", command=self.agregar_tarea).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="COMPLETAR", command=self.marcar_completada).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="ELIMINAR", command=self.eliminar_tarea).pack(side=tk.LEFT, padx=5)

        ttk.Label(main_frame, text="Listado de Misiones:").pack(anchor=tk.W, pady=(10, 5))

        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.lista_tareas = tk.Listbox(list_frame, height=15, selectmode=tk.SINGLE, bg=self.bg_color,
                                       fg=self.text_color, selectbackground=self.button_color, font=("Courier New", 10))
        self.lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.lista_tareas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_tareas.config(yscrollcommand=scrollbar.set)

        ttk.Label(main_frame, text="* Doble clic para marcar como completada *", font=("Arial", 8)).pack(pady=(10, 0))

    def configurar_eventos(self):
        self.entrada_tarea.bind("<Return>", lambda e: self.agregar_tarea())
        self.lista_tareas.bind("<Double-Button-1>", lambda e: self.marcar_completada())
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)

    def agregar_tarea(self):
        tarea_texto = self.entrada_tarea.get().strip()
        if tarea_texto:
            self.tareas.append({"texto": tarea_texto, "completada": False})
            self.entrada_tarea.delete(0, tk.END)
            self.actualizar_lista()
            self.guardar_tareas()
        else:
            messagebox.showwarning("¡ATENCIÓN!", "Debe ingresar una misión válida")

    def marcar_completada(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index]["completada"] = not self.tareas[index]["completada"]
            self.actualizar_lista()
            self.guardar_tareas()

    def eliminar_tarea(self):
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            if messagebox.askyesno("Confirmar Eliminación", f"¿Eliminar la misión: {self.tareas[index]['texto']}?"):
                del self.tareas[index]
                self.actualizar_lista()
                self.guardar_tareas()

    def actualizar_lista(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            estado = "[✓] " if tarea["completada"] else "[ ] "
            texto_tarea = f"{estado}{tarea['texto']}"
            self.lista_tareas.insert(tk.END, texto_tarea)

    def cargar_tareas(self):
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "rb") as f:
                    return pickle.load(f)
        except:
            messagebox.showerror("Error", "No se pudieron cargar las misiones")
        return []

    def guardar_tareas(self):
        try:
            with open(self.data_file, "wb") as f:
                pickle.dump(self.tareas, f)
        except:
            messagebox.showerror("Error", "No se pudieron guardar las misiones")

    def cerrar_aplicacion(self):
        self.guardar_tareas()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
