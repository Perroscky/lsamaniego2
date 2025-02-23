import pickle  # Importamos pickle para poder guardar y cargar objetos Python en archivos

# Definimos la clase producto que representa cada ítem del inventario
class Producto:

    # Constructor que inicializa un nuevo producto con sus atributos básicos
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en inventario
        self.precio = precio  # Precio del producto

    # Métodos getter para obtener los atributos del producto
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos setter para modificar los atributos que pueden cambiar
    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    # Metodo para representar el producto como texto (usado al imprimir)
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

# Definimos la clase Inventario que gestionará la colección de productos
class Inventario:
    # Constructor que inicializa un inventario vacío
    def __init__(self):
        # Usamos un diccionario porque permite búsqueda rápida por ID (clave)
        self.productos = {}

        # Metodo para agregar un nuevo producto al inventario

    def agregar_producto(self, producto):
        # Verificamos si ya existe un producto con ese ID
        if producto.get_id() in self.productos:
            print(f"Error: Ya existe un producto con el ID {producto.get_id()}")
            return False
        # Agregamos el producto al diccionario usando su ID como clave
        self.productos[producto.get_id()] = producto
        print(f"Producto '{producto.get_nombre()}' agregado correctamente.")
        return True

    # Metodo para eliminar un producto del inventario
    def eliminar_producto(self, id_producto):
        # Verificamos si existe un producto con ese ID
        if id_producto in self.productos:
            nombre = self.productos[id_producto].get_nombre()
            # Eliminamos el producto del diccionario
            del self.productos[id_producto]
            print(f"Producto '{nombre}' eliminado correctamente.")
            return True
        print(f"Error: No se encontró un producto con ID {id_producto}")
        return False

    # Metodo para actualizar la cantidad de un producto
    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        # Verificamos si existe un producto con ese ID
        if id_producto in self.productos:
            # Actualizamos la cantidad utilizando el metodo setter
            self.productos[id_producto].set_cantidad(nueva_cantidad)
            print(f"Cantidad actualizada para '{self.productos[id_producto].get_nombre()}'")
            return True
        print(f"Error: No se encontró un producto con ID {id_producto}")
        return False

    # Metodo para actualizar el precio de un producto
    def actualizar_precio(self, id_producto, nuevo_precio):
        # Verificamos si existe un producto con ese ID
        if id_producto in self.productos:
            # Actualizamos el precio utilizando el metodo setter
            self.productos[id_producto].set_precio(nuevo_precio)
            print(f"Precio actualizado para '{self.productos[id_producto].get_nombre()}'")
            return True
        print(f"Error: No se encontró un producto con ID {id_producto}")
        return False

    # Metodo para buscar productos por nombre (búsqueda parcial)
    def buscar_por_nombre(self, nombre):
        productos_encontrados = []
        # Iteramos todos los productos del diccionario (values devuelve solo los valores)
        for producto in self.productos.values():
            # Comprobamos si el texto de búsqueda está contenido en el nombre (ignorando mayúsculas/minúsculas)
            if nombre.lower() in producto.get_nombre().lower():
                productos_encontrados.append(producto)
        return productos_encontrados

    # Metodo para mostrar todos los productos del inventario
    def mostrar_todos(self):
        # Verificamos si el inventario está vacío
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("\n=== LISTADO DE PRODUCTOS ===")
        # Iteramos y mostramos cada producto
        for producto in self.productos.values():
            print(producto)


# Función para guardar el inventario en un archivo usando pickle
def guardar_inventario(inventario, nombre_archivo="inventario.dat"):
    try:
        # Abrimos el archivo en modo escritura binaria
        with open(nombre_archivo, 'wb') as archivo:
            # Guardamos el diccionario de productos
            pickle.dump(inventario.productos, archivo)
        print(f"Inventario guardado correctamente en '{nombre_archivo}'")
        return True
    except Exception as e:
        # Capturamos cualquier error que pueda ocurrir al guardar
        print(f"Error al guardar el inventario: {e}")
        return False

# Función para cargar el inventario desde un archivo
def cargar_inventario(inventario, nombre_archivo="inventario.dat"):
    try:
        # Abrimos el archivo en modo lectura binaria
        with open(nombre_archivo, 'rb') as archivo:
            # Cargamos el diccionario de productos
            inventario.productos = pickle.load(archivo)
        print(f"Inventario cargado correctamente desde '{nombre_archivo}'")
        return True
    except FileNotFoundError:
        # Error específico si el archivo no existe
        print(f"Archivo '{nombre_archivo}' no encontrado. Se inicia con inventario vacío.")
        return False
    except Exception as e:
        # Cualquier otro error que pueda ocurrir
        print(f"Error al cargar el inventario: {e}")
        return False

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad")
    print("4. Actualizar precio")
    print("5. Buscar producto por nombre")
    print("6. Mostrar todos los productos")
    print("7. Guardar inventario")
    print("8. Cargar inventario")
    print("9. Salir")
    return input("Seleccione una opción: ")

# Función principal que ejecuta el programa
def main():
    # Creamos una instancia de Inventario
    inventario = Inventario()

    # Intentamos cargar un inventario existente al iniciar el programa
    cargar_inventario(inventario)

    # Bucle principal del programa
    while True:
        # Mostramos el menú y obtenemos la opción seleccionada
        opcion = mostrar_menu()

        # Opción 1: Agregar un producto
        if opcion == "1":
            try:
                # Solicitamos los datos del nuevo producto
                id = int(input("ID del producto: "))
                nombre = input("Nombre del producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                # Creamos el producto y lo agregamos al inventario
                producto = Producto(id, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                # Capturamos errores si el usuario ingresa datos no numéricos
                print("Error: Por favor ingrese valores numéricos válidos.")

        # Opción 2: Eliminar un producto
        elif opcion == "2":
            try:
                # Solicitamos el ID del producto a eliminar
                id = int(input("ID del producto a eliminar: "))
                inventario.eliminar_producto(id)
            except ValueError:
                print("Error: Por favor ingrese un ID válido.")

        # Opción 3: Actualizar cantidad de un producto
        elif opcion == "3":
            try:
                # Solicitamos el ID y la nueva cantidad
                id = int(input("ID del producto: "))
                cantidad = int(input("Nueva cantidad: "))
                inventario.actualizar_cantidad(id, cantidad)
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos.")

        # Opción 4: Actualizar precio de un producto
        elif opcion == "4":
            try:
                # Solicitamos el ID y el nuevo precio
                id = int(input("ID del producto: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_precio(id, precio)
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos.")

        # Opción 5: Buscar productos por nombre
        elif opcion == "5":
            nombre = input("Nombre a buscar: ")
            productos = inventario.buscar_por_nombre(nombre)
            # Verificamos si se encontraron productos
            if productos:
                print(f"\nSe encontraron {len(productos)} productos:")
                for producto in productos:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        # Opción 6: Mostrar todos los productos
        elif opcion == "6":
            inventario.mostrar_todos()

        # Opción 7: Guardar inventario en archivo
        elif opcion == "7":
            guardar_inventario(inventario)

        # Opción 8: Cargar inventario desde archivo
        elif opcion == "8":
            cargar_inventario(inventario)

        # Opción 9: Salir del programa
        elif opcion == "9":
            # Preguntamos si desea guardar antes de salir
            print("¿Desea guardar el inventario antes de salir?")
            respuesta = input("S/N: ").upper()
            if respuesta == "S":
                guardar_inventario(inventario)
            print("¡Gracias por usar el Sistema de Gestión de Inventario!")
            break

        # Manejo de opciones inválidas
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Punto de entrada del programa
# Esto asegura que la función main() solo se ejecute si este archivo se ejecuta directamente
# y no cuando se importa desde otro archivo
if __name__ == "__main__":
    main()