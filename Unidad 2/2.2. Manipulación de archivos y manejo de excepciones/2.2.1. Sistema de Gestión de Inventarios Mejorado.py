import os
import json

#SISTEMA DE GESTIÓN DE INVENTARIOS MEJORADO
class Producto:
    """
    Clase que representa un producto individual en el inventario.
    """

    def __init__(self, id, nombre, cantidad, precio):
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self._cantidad = cantidad
        else:
            raise ValueError("La cantidad no puede ser negativa")

    def set_precio(self, precio):
        if precio >= 0:
            self._precio = precio
        else:
            raise ValueError("El precio no puede ser negativo")

    def to_dict(self):
        """
        Convierte un objeto Producto a un diccionario para serializarlo.
        """
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crea un objeto Producto a partir de un diccionario.
        """
        return cls(data['id'], data['nombre'], data['cantidad'], data['precio'])

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Cantidad: {self._cantidad}, Precio: ${self._precio:.2f}"

class Inventario:
    """
    Clase que gestiona la colección de productos.
    """

    def __init__(self, archivo='inventario.txt'):
        """
        Inicializa el inventario y carga los productos desde el archivo de almacenamiento.
        """
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga el inventario desde el archivo (si existe). Si el archivo no se encuentra,
        se informa al usuario y no se genera error.
        """
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    productos_data = json.load(file)  # Carga el contenido JSON
                    self.productos = [Producto.from_dict(p) for p in productos_data]  # Convierte los datos a objetos Producto
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error al cargar el archivo de inventario: {e}")
        else:
            print(f"Archivo '{self.archivo}' no encontrado. Se creará uno nuevo.")

    def guardar_inventario(self):
        """
        Guarda el inventario en el archivo de texto (serialización a formato JSON).
        Utiliza un manejo adecuado de excepciones para posibles errores de archivo.
        """
        try:
            with open(self.archivo, 'w') as file:
                productos_data = [p.to_dict() for p in self.productos]  # Convierte los productos a formato de diccionario
                json.dump(productos_data, file, indent=4)  # Serializa los productos en el archivo
            print("Inventario guardado exitosamente en el archivo.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el archivo de inventario: {e}")

    def añadir_producto(self, id, nombre, cantidad, precio):
        """
        Añade un nuevo producto al inventario y lo guarda en el archivo.
        """
        if any(p.get_id() == id for p in self.productos):
            raise ValueError(f"El ID {id} ya existe en el inventario")
        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        self.guardar_inventario()  # Guarda cambios después de añadir el producto
        return "Producto añadido exitosamente"

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario y actualiza el archivo.
        """
        for i, producto in enumerate(self.productos):
            if producto.get_id() == id:
                self.productos.pop(i)  # Elimina el producto
                self.guardar_inventario()  # Guarda cambios después de eliminar el producto
                return "Producto eliminado exitosamente"
        raise ValueError(f"No se encontró producto con ID {id}")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad y/o precio de un producto y guarda los cambios en el archivo.
        """
        for producto in self.productos:
            if producto.get_id() == id:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                self.guardar_inventario()  # Guarda cambios después de la actualización
                return "Producto actualizado exitosamente"
        raise ValueError(f"No se encontró producto con ID {id}")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por nombre (de forma parcial y case-insensitive).
        """
        productos_encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return productos_encontrados

    def mostrar_inventario(self):
        """
        Devuelve todos los productos en el inventario.
        """
        return self.productos

def menu_principal():
    """
    Interfaz de usuario del sistema de gestión de inventarios.
    """
    inventario = Inventario()

    while True:
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
                id = int(input("Ingrese ID del producto: "))
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                print(inventario.añadir_producto(id, nombre, cantidad, precio))

            elif opcion == "2":
                id = int(input("Ingrese ID del producto a eliminar: "))
                print(inventario.eliminar_producto(id))

            elif opcion == "3":
                id = int(input("Ingrese ID del producto a actualizar: "))
                actualizar_cantidad = input("¿Desea actualizar la cantidad? (s/n): ").lower() == 's'
                actualizar_precio = input("¿Desea actualizar el precio? (s/n): ").lower() == 's'

                nueva_cantidad = int(input("Ingrese nueva cantidad: ")) if actualizar_cantidad else None
                nuevo_precio = float(input("Ingrese nuevo precio: ")) if actualizar_precio else None

                print(inventario.actualizar_producto(id, nueva_cantidad, nuevo_precio))

            elif opcion == "4":
                nombre = input("Ingrese nombre o parte del nombre a buscar: ")
                productos = inventario.buscar_por_nombre(nombre)
                if productos:
                    print("\nProductos encontrados:")
                    for producto in productos:
                        print(producto)
                else:
                    print("No se encontraron productos con ese nombre")

            elif opcion == "5":
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
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    menu_principal()
