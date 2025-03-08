# Sistema de Biblioteca Digital

# Clase para representar un libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Guardo el título y autor en una tupla porque no van a cambiar
        self.datos_libro = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False  # Al principio no está prestado

    # Para obtener el título
    def get_titulo(self):
        return self.datos_libro[0]

    # Para obtener el autor
    def get_autor(self):
        return self.datos_libro[1]

    # Para mostrar la información del libro
    def mostrar_info(self):
        if self.prestado:
            estado = "Prestado"
        else:
            estado = "Disponible"
        return f"Libro: {self.get_titulo()} - Autor: {self.get_autor()} - Categoría: {self.categoria} - ISBN: {self.isbn} - Estado: {estado}"


# Clase para representar un usuario
class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
        # Lista vacía para guardar los libros prestados
        self.libros_prestados = []

    # Para añadir un libro prestado
    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    # Para devolver un libro
    def devolver_libro(self, libro):
        # Compruebo si el libro está en la lista
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            return True
        return False

    # Para ver qué libros tiene prestados
    def ver_libros_prestados(self):
        return self.libros_prestados

    # Para mostrar información del usuario
    def mostrar_info(self):
        return f"Usuario: {self.nombre} (ID: {self.id}) - Tiene {len(self.libros_prestados)} libros prestados"


# Clase para gestionar la biblioteca
class Biblioteca:
    def __init__(self):
        # Diccionario para guardar los libros
        self.libros = {}
        # Diccionario para guardar los usuarios
        self.usuarios = {}
        # Conjunto para los IDs de usuarios
        self.ids_usuarios = set()

    # Para añadir un libro nuevo
    def añadir_libro(self, titulo, autor, categoria, isbn):
        # Compruebo si ya existe un libro con ese ISBN
        if isbn in self.libros:
            print(f"Error: Ya hay un libro con ISBN {isbn}")
            return False

        # Creo el libro nuevo
        nuevo_libro = Libro(titulo, autor, categoria, isbn)
        # Lo guardo en el diccionario
        self.libros[isbn] = nuevo_libro
        print(f"Se ha añadido el libro: {nuevo_libro.mostrar_info()}")
        return True

    # Para quitar un libro
    def quitar_libro(self, isbn):
        # Compruebo si existe el libro
        if isbn not in self.libros:
            print(f"Error: No hay ningún libro con ISBN {isbn}")
            return False

        libro = self.libros[isbn]
        # Compruebo si está prestado
        if libro.prestado:
            print(f"Error: No se puede quitar el libro '{libro.get_titulo()}' porque está prestado")
            return False

        # Borro el libro del diccionario
        del self.libros[isbn]
        print(f"Se ha quitado el libro: '{libro.get_titulo()}'")
        return True

    # Para registrar un usuario nuevo
    def registrar_usuario(self, nombre, id):
        # Compruebo si ya existe un usuario con ese ID
        if id in self.ids_usuarios:
            print(f"Error: Ya hay un usuario con ID {id}")
            return False

        # Creo el usuario nuevo
        nuevo_usuario = Usuario(nombre, id)
        # Lo guardo en el diccionario
        self.usuarios[id] = nuevo_usuario
        # Añado el ID al conjunto
        self.ids_usuarios.add(id)
        print(f"Se ha registrado el usuario: {nuevo_usuario.mostrar_info()}")
        return True

    # Para dar de baja a un usuario
    def dar_baja_usuario(self, id):
        # Compruebo si existe el usuario
        if id not in self.ids_usuarios:
            print(f"Error: No hay ningún usuario con ID {id}")
            return False

        usuario = self.usuarios[id]
        # Compruebo si tiene libros prestados
        if len(usuario.libros_prestados) > 0:
            print(f"Error: El usuario {usuario.nombre} tiene que devolver {len(usuario.libros_prestados)} libros")
            return False

        # Borro el usuario del diccionario
        del self.usuarios[id]
        # Quito el ID del conjunto
        self.ids_usuarios.remove(id)
        print(f"Se ha dado de baja al usuario: {usuario.nombre}")
        return True

    # Para prestar un libro
    def prestar_libro(self, isbn, id_usuario):
        # Compruebo si existe el libro
        if isbn not in self.libros:
            print(f"Error: No hay ningún libro con ISBN {isbn}")
            return False

        # Compruebo si existe el usuario
        if id_usuario not in self.ids_usuarios:
            print(f"Error: No hay ningún usuario con ID {id_usuario}")
            return False

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        # Compruebo si el libro está disponible
        if libro.prestado:
            print(f"Error: El libro '{libro.get_titulo()}' ya está prestado")
            return False

        # Marco el libro como prestado
        libro.prestado = True
        # Añado el libro a la lista del usuario
        usuario.prestar_libro(libro)
        print(f"El libro '{libro.get_titulo()}' ha sido prestado a {usuario.nombre}")
        return True

    # Para devolver un libro
    def devolver_libro(self, isbn, id_usuario):
        # Compruebo si existe el libro
        if isbn not in self.libros:
            print(f"Error: No hay ningún libro con ISBN {isbn}")
            return False

        # Compruebo si existe el usuario
        if id_usuario not in self.ids_usuarios:
            print(f"Error: No hay ningún usuario con ID {id_usuario}")
            return False

        libro = self.libros[isbn]
        usuario = self.usuarios[id_usuario]

        # Compruebo si el libro está prestado
        if not libro.prestado:
            print(f"Error: El libro '{libro.get_titulo()}' no está prestado")
            return False

        # Intento devolver el libro
        if not usuario.devolver_libro(libro):
            print(f"Error: El usuario {usuario.nombre} no tiene el libro '{libro.get_titulo()}'")
            return False

        # Marco el libro como disponible
        libro.prestado = False
        print(f"El libro '{libro.get_titulo()}' ha sido devuelto por {usuario.nombre}")
        return True

    # Para buscar libros por título
    def buscar_por_titulo(self, titulo):
        titulo = titulo.lower()  # Paso a minúsculas para buscar mejor
        resultados = []

        # Busco en todos los libros
        for isbn in self.libros:
            libro = self.libros[isbn]
            if titulo in libro.get_titulo().lower():
                resultados.append(libro)

        return resultados

    # Para buscar libros por autor
    def buscar_por_autor(self, autor):
        autor = autor.lower()  # Paso a minúsculas para buscar mejor
        resultados = []

        # Busco en todos los libros
        for isbn in self.libros:
            libro = self.libros[isbn]
            if autor in libro.get_autor().lower():
                resultados.append(libro)

        return resultados

    # Para buscar libros por categoría
    def buscar_por_categoria(self, categoria):
        categoria = categoria.lower()  # Paso a minúsculas para buscar mejor
        resultados = []

        # Busco en todos los libros
        for isbn in self.libros:
            libro = self.libros[isbn]
            if categoria == libro.categoria.lower():
                resultados.append(libro)

        return resultados

    # Para ver los libros prestados a un usuario
    def ver_libros_usuario(self, id_usuario):
        # Compruebo si existe el usuario
        if id_usuario not in self.ids_usuarios:
            print(f"Error: No hay ningún usuario con ID {id_usuario}")
            return None

        usuario = self.usuarios[id_usuario]
        return usuario.ver_libros_prestados()


# Función para probar el sistema
def probar_biblioteca():
    print("===== PRUEBA DE LA BIBLIOTECA DIGITAL =====")

    # Creo una biblioteca
    mi_biblioteca = Biblioteca()

    # Añado algunos libros
    mi_biblioteca.añadir_libro("Don Quijote", "Miguel de Cervantes", "Novela", "123456")
    mi_biblioteca.añadir_libro("La Bella y la Bestia", "Gabrielle-Suzanne de Villeneuve", "Cuento", "789012")
    mi_biblioteca.añadir_libro("Blanca Nieves y los 7 enanitos", "Hermanos Grimm", "Cuento de hadas", "345678")

    print("\n--- Prueba de búsqueda ---")
    print("Buscar 'quijote':")
    libros_encontrados = mi_biblioteca.buscar_por_titulo("quijote")
    for libro in libros_encontrados:
        print(f"  - {libro.mostrar_info()}")

    print("\nBuscar 'cuento':")
    libros_encontrados = mi_biblioteca.buscar_por_categoria("cuento")
    for libro in libros_encontrados:
        print(f"  - {libro.mostrar_info()}")

    # Registro algunos usuarios
    print("\n--- Prueba de usuarios ---")
    mi_biblioteca.registrar_usuario("Luis Samaniego", "U1")
    mi_biblioteca.registrar_usuario("Adrian Samaniego", "U2")
    mi_biblioteca.registrar_usuario("Liham Samaniego", "U3")

    # Pruebo a registrar un usuario con ID repetido
    mi_biblioteca.registrar_usuario("Pedro López", "U1")

    # Pruebo a prestar libros
    print("\n--- Prueba de préstamos ---")
    mi_biblioteca.prestar_libro("123456", "U1")
    mi_biblioteca.prestar_libro("345678", "U2")
    mi_biblioteca.prestar_libro("789012", "U3")

    # Pruebo a devolver libros
    print("\n--- Prueba de devoluciones ---")
    mi_biblioteca.devolver_libro("123456", "U1")
    mi_biblioteca.devolver_libro("345678", "U2")

    # Intento quitar un libro prestado
    print("\n--- Intento de quitar un libro prestado ---")
    mi_biblioteca.quitar_libro("789012")

    # Quitar un libro disponible
    mi_biblioteca.quitar_libro("345678")

    # Intentar dar de baja a un usuario con libros prestados
    print("\n--- Intento de baja de usuario con libros ---")
    mi_biblioteca.dar_baja_usuario("U1")

    # Intentar dar de baja a un usuario sin libros prestados
    print("\n--- Baja de usuario sin libros prestados ---")
    mi_biblioteca.dar_baja_usuario("U3")


# Ejecutar la prueba
probar_biblioteca()
