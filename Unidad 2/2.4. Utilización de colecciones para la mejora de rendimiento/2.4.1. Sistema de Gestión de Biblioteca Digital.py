#SISTEMA DE GESTION DE UNA BIBLIOTECA
import pickle

# Definimos la clase Libro con atributos inmutables usando tuplas
class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        self.isbn = isbn  # ISBN único del libro
        self.titulo_autor = (titulo, autor)  # Tupla inmutable con título y autor
        self.categoria = categoria  # Categoría del libro

    def __repr__(self):
        titulo, autor = self.titulo_autor  # Desempaquetamos la tupla
        return f"'{titulo}' de {autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# Definimos la clase Usuario con un ID único para cada usuario
class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario  # ID único del usuario
        self.nombre = nombre  # Nombre del usuario
        self.libros_prestados = []  # Lista para almacenar los libros prestados

    def __repr__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def agregar_libro(self, libro):
        """Añadir un libro a la lista de libros prestados"""
        self.libros_prestados.append(libro)

    def quitar_libro(self, libro):
        """Quitar un libro de la lista de libros prestados"""
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)


# Definimos la clase Biblioteca que gestionará los libros y los usuarios
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros por ISBN (clave) y Libro (valor)
        self.usuarios = set()  # Conjunto para almacenar usuarios (aseguramos que sean únicos)

    def agregar_libro(self, libro):
        """Añadir un libro a la biblioteca"""
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo_autor[0]}' añadido a la biblioteca.")
        else:
            print(f"El libro '{libro.titulo_autor[0]}' ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        """Eliminar un libro de la biblioteca por ISBN"""
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} ha sido eliminado de la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        """Registrar un nuevo usuario en la biblioteca"""
        if usuario.id_usuario not in [u.id_usuario for u in self.usuarios]:
            self.usuarios.add(usuario)
            print(f"Usuario {usuario.nombre} registrado exitosamente.")
        else:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        """Dar de baja un usuario"""
        usuario_a_borrar = None
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                usuario_a_borrar = usuario
                break
        if usuario_a_borrar:
            self.usuarios.remove(usuario_a_borrar)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    def prestar_libro(self, id_usuario, isbn):
        """Prestar un libro a un usuario"""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = self.libros.get(isbn)

        if usuario and libro:
            if libro not in usuario.libros_prestados:
                usuario.agregar_libro(libro)
                print(f"El libro '{libro.titulo_autor[0]}' ha sido prestado a {usuario.nombre}.")
            else:
                print(f"El libro '{libro.titulo_autor[0]}' ya está prestado a {usuario.nombre}.")
        else:
            print(f"Usuario o libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        """Devolver un libro prestado por un usuario"""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = self.libros.get(isbn)

        if usuario and libro:
            if libro in usuario.libros_prestados:
                usuario.quitar_libro(libro)
                print(f"El libro '{libro.titulo_autor[0]}' ha sido devuelto por {usuario.nombre}.")
            else:
                print(f"El libro '{libro.titulo_autor[0]}' no está prestado a {usuario.nombre}.")
        else:
            print(f"Usuario o libro no encontrado.")

    def buscar_libro(self, criterio):
        """Buscar libros por título, autor o categoría"""
        resultados = [libro for libro in self.libros.values() if
                      criterio.lower() in libro.titulo_autor[0].lower() or
                      criterio.lower() in libro.titulo_autor[1].lower() or
                      criterio.lower() in libro.categoria.lower()]

        if resultados:
            print("Resultados de búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con el criterio.")

    def listar_libros_prestados(self, id_usuario):
        """Listar los libros prestados a un usuario"""
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)

        if usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"Usuario con ID {id_usuario} no encontrado.")

    def ver_usuarios_registrados(self):
        """Mostrar todos los usuarios registrados"""
        if self.usuarios:
            print("Usuarios registrados:")
            for usuario in self.usuarios:
                print(usuario)
        else:
            print("No hay usuarios registrados.")

    def ver_libros_disponibles(self):
        """Mostrar todos los libros disponibles en la biblioteca"""
        if self.libros:
            print("Libros disponibles en la biblioteca:")
            for libro in self.libros.values():
                print(libro)
        else:
            print("No hay libros disponibles en la biblioteca.")

    def guardar_datos(self, archivo):
        """Guardar los datos de la biblioteca en un archivo .dat"""
        with open(archivo, 'wb') as f:
            pickle.dump(self.libros, f)
            pickle.dump(self.usuarios, f)
        print("Datos guardados en el archivo.")

    def cargar_datos(self, archivo):
        """Cargar los datos de la biblioteca desde un archivo .dat"""
        try:
            with open(archivo, 'rb') as f:
                self.libros = pickle.load(f)
                self.usuarios = pickle.load(f)
            print("Datos cargados desde el archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo, iniciando con datos vacíos.")


# Función para mostrar el menú
def mostrar_menu():
    print("\n-- Menú de Biblioteca --")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar libros prestados")
    print("9. Ver usuarios registrados")
    print("10. Ver libros disponibles")
    print("11. Guardar datos")
    print("12. Cargar datos")
    print("13. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


# Función para ejecutar las operaciones
def ejecutar_operaciones():
    archivo = "biblioteca.dat"  # Nombre del archivo donde se guardarán los datos
    biblioteca = Biblioteca()
    biblioteca.cargar_datos(archivo)  # Cargar los datos al inicio

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            isbn = input("Ingrese el ISBN del libro: ")
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("Ingrese el ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            id_usuario = int(input("Ingrese el ID del usuario: "))
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = Usuario(id_usuario, nombre)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = int(input("Ingrese el ID del usuario a dar de baja: "))
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            id_usuario = int(input("Ingrese el ID del usuario que pide el libro: "))
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            id_usuario = int(input("Ingrese el ID del usuario que devuelve el libro: "))
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            criterio = input("Ingrese el criterio de búsqueda (título, autor o categoría): ")
            biblioteca.buscar_libro(criterio)

        elif opcion == "8":
            id_usuario = int(input("Ingrese el ID del usuario para listar libros prestados: "))
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":
            biblioteca.ver_usuarios_registrados()

        elif opcion == "10":
            biblioteca.ver_libros_disponibles()

        elif opcion == "11":
            biblioteca.guardar_datos(archivo)

        elif opcion == "12":
            biblioteca.cargar_datos(archivo)

        elif opcion == "13":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


# Ejecutamos las operaciones
ejecutar_operaciones()
