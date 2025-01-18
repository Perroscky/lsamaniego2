class Recurso:
    """
    Clase que demuestra el uso de constructor y destructor
    """

    def __init__(self, nombre):
        """
        Constructor: Inicializa el recurso y abre una conexión

        :param nombre: Nombre del recurso
        """
        self.nombre = nombre
        print(f"Recurso '{self.nombre}' creado. Abriendo conexión...")
        self.conexion = True

    def __del__(self):
        """
        Destructor: Realiza limpieza cerrando la conexión
        """
        if self.conexion:
            print(f"Destructor: Cerrando conexión para '{self.nombre}'")
            self.conexion = False


class GestorRecursos:
    """
    Clase que gestiona múltiples recursos
    """

    def __init__(self, max_recursos=3):
        """
        Constructor: Inicializa el gestor con una lista de recursos

        :param max_recursos: Número máximo de recursos a gestionar
        """
        self.max_recursos = max_recursos
        self.recursos = []

        # Crear recursos con nombres descriptivos
        nombres_recursos = [
            "Base de Datos Principal",
            "Conexión de Red",
            "Archivo de Configuración"
        ]

        for i in range(min(max_recursos, len(nombres_recursos))):
            self.recursos.append(Recurso(nombres_recursos[i]))

    def __del__(self):
        """
        Destructor: Limpia todos los recursos al eliminar el gestor
        """
        print("Destructor de GestorRecursos: Limpiando todos los recursos")
        del self.recursos


def main():
    """
    Función principal para demostrar el uso de constructores y destructores
    """
    print("Creando gestor de recursos...")
    gestor = GestorRecursos(2)

    print("\nElimimando referencias...")
    del gestor


if __name__ == "__main__":
    main()

