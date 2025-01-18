# Clase base (Padre)
class Animal:
    # Constructor de la clase base
    def __init__(self, nombre, edad):
        # Encapsulación: Los atributos se definen como privados (con __) para evitar acceso directo
        self.__nombre = nombre  # Atributo privado
        self.__edad = edad  # Atributo privado

    # Métodos getter para acceder a los atributos privados
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método que será sobrescrito por las subclases (polimorfismo)
    def hacer_sonido(self):
        return "Este animal hace un sonido."


# Clase derivada (Hija) que hereda de Animal
class Elefante(Animal):
    # Constructor de la clase derivada
    def __init__(self, nombre, edad, tamaño):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, edad)
        self.__tamaño = tamaño  # Atributo específico de la clase Elefante

    # Método getter para obtener el tamaño
    def get_tamaño(self):
        return self.__tamaño

    # Sobrescribimos el método hacer_sonido para el elefante (polimorfismo)
    def hacer_sonido(self):
        return "¡Prrrrr! (Sonido de elefante)"


# Otra clase derivada (Hija) que hereda de Animal
class Leon(Animal):
    # Constructor de la clase derivada
    def __init__(self, nombre, edad, melena):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, edad)
        self.__melena = melena  # Atributo específico de la clase León

    # Método getter para obtener la melena
    def get_melena(self):
        return self.__melena

    # Sobrescribimos el método hacer_sonido para el león (polimorfismo)
    def hacer_sonido(self):
        return "¡Rugido! (Sonido de león)"


# Creación de objetos de las clases Elefante y León (instanciación)
mi_elefante = Elefante("Rocky", 25, "Grande")
mi_leon = Leon("Pelusa", 15, "Espesa")

# Llamamos al método hacer_sonido de cada objeto (demostrando polimorfismo)
print(f"{mi_elefante.get_nombre()} dice: {mi_elefante.hacer_sonido()}")  # Polimorfismo
print(f"{mi_leon.get_nombre()} dice: {mi_leon.hacer_sonido()}")  # Polimorfismo

# Mostramos los detalles del elefante y el león utilizando métodos getter
print(f"{mi_elefante.get_nombre()} tiene {mi_elefante.get_edad()} años y su tamaño es {mi_elefante.get_tamaño()}.")
print(f"{mi_leon.get_nombre()} tiene {mi_leon.get_edad()} años y su melena es {mi_leon.get_melena()}.")
