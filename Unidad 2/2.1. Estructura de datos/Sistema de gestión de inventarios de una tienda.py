# SITEMA DE GESTIÓN DE INVENTARIOS
# El sistema implementa un CRUD básico para gestionar productos en un inventario
# utilizando programación orientada a objetos.

class Producto:
    """
    Clase que representa un producto individual en el inventario.
    Implementa el patrón de encapsulamiento usando propiedades privadas con getters y setters.
    """

    def __init__(self, id, nombre, cantidad, precio):
        # Uso de atributos protegidos (single underscore) para encapsulamiento
        self._id = id  # ID único del producto
        self._nombre = nombre  # Nombre del producto
        self._cantidad = cantidad  # Cantidad en inventario
        self._precio = precio  # Precio unitario

    # Getters: Proporcionan acceso controlado a los atributos privados
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters: Permiten modificar atributos con validación
    def set_cantidad(self, cantidad):
        # Validación: La cantidad no puede ser negativa
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")

    def set_precio(self, precio):
        # Validación: El precio no puede ser negativo
        if precio >= 0:
            self._precio = precio
        else:
            raise ValueError("El precio no puede ser negativo")

    def __str__(self):
        # Sobreescritura del método str para mostrar información del producto de forma comprensible
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"

class Inventario:
    """
    Clase que gestiona la colección de productos.
    Implementa operaciones CRUD (Create, Read, Update, Delete) sobre los productos.
    """

    def __init__(self):
        # Inicializa una lista vacía para almacenar los productos
        self.productos = []

    def añadir_producto(self, id, nombre, cantidad, precio):
        """
        Añade un nuevo producto al inventario verificando que el ID sea único.
        Raises:
            ValueError: Si el ID ya existe en el inventario
        """
        # Verificación de ID único usando comprensión de listas
        if any(p.get_id() == id for p in self.productos):
            raise ValueError(f"El ID {id} ya existe en el inventario")

        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        return "Producto añadido exitosamente"

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        Raises:
            ValueError: Si no se encuentra el ID especificado
        """
        # Uso de enumerate para obtener índice y valor simultáneamente
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id:
                self.productos.pop(i)
                return "Producto eliminado exitosamente"
        raise ValueError(f"No se encontró producto con ID {id}")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad y/o precio de un producto.
        Permite actualizar uno o ambos valores usando parámetros opcionales.
        """
        for producto in self.productos:
            if producto.get_id() == id:
                # Actualización condicional: solo si se proporciona un nuevo valor
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                return "Producto actualizado exitosamente"
        raise ValueError(f"No se encontró producto con ID {id}")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por nombre, incluyendo coincidencias parciales.
        Implementa búsqueda case-insensitive para mejor usabilidad.
        """
        # Uso de comprensión de listas para búsqueda case-insensitive
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return productos_encontrados

    def mostrar_inventario(self):
        """
        Retorna la lista completa de productos en el inventario.
        """
        return self.productos

def menu_principal():
    """
    Función principal que implementa la interfaz de usuario en consola.
    Maneja la interacción con el usuario y el control de errores.
    """
    inventario = Inventario()

    while True:
        # Menú principal con todas las operaciones disponibles
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIOS ===")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar productos por nombre")
        print("5. Mostrar todo el inventario")
        print("6. Salir")

        opcion = input("\nSeleccione una opción (1-6): ")

        try:
            if opcion == "1":
                # Captura y validación de datos para nuevo producto
                id = int(input("Ingrese ID del producto: "))
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                print(inventario.añadir_producto(id, nombre, cantidad, precio))

            elif opcion == "2":
                # Eliminación de producto por ID
                id = int(input("Ingrese ID del producto a eliminar: "))
                print(inventario.eliminar_producto(id))

            elif opcion == "3":
                # Actualización selectiva de cantidad y/o precio
                id = int(input("Ingrese ID del producto a actualizar: "))
                actualizar_cantidad = input("¿Desea actualizar la cantidad? (s/n): ").lower() == 's'
                actualizar_precio = input("¿Desea actualizar el precio? (s/n): ").lower() == 's'

                nueva_cantidad = int(input("Ingrese nueva cantidad: ")) if actualizar_cantidad else None
                nuevo_precio = float(input("Ingrese nuevo precio: ")) if actualizar_precio else None

                print(inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio))

            elif opcion == "4":
                # Búsqueda flexible por nombre
                nombre = input("Ingrese nombre o parte del nombre a buscar: ")
                productos = inventario.buscar_por_nombre(nombre)
                if productos:
                    print("\nProductos encontrados:")
                    for producto in productos:
                        print(producto)
                else:
                    print("No se encontraron productos con ese nombre")

            elif opcion == "5":
                # Visualización del inventario completo
                productos = inventario.mostrar_inventario()
                if productos:
                    print("\nInventario completo:")
                    for producto in productos:
                        print(producto)
                else:
                    print("El inventario está vacío")

            elif opcion == "6":
                print("¡Gracias por usar el sistema!")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 6")

        except ValueError as e:
            # Manejo de errores de validación
            print(f"Error: {e}")
        except Exception as e:
            # Manejo de errores inesperados
            print(f"Error inesperado: {e}")

# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()