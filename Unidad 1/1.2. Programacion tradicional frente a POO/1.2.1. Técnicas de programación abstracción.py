from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def hacer_sonido(self):
        pass

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")

# Crear objetos
gato = Gato("Whiskers", 2)
perro = Perro("Buddy", 5)

# Llamar a los métodos
gato.hacer_sonido()
perro.hacer_sonido()
# EXPLICACION DEL CODIGO
# ABC y abstractmethod: Estas herramientas de la librería abc (Abstract Base Classes) nos permiten definir clases
# y métodos abstractos.
# Clase Animal: Es la clase base que define los atributos y el método hacer_sonido que todas las clases hijas
#  deben implementar.
# Clases Gato y Perro: Heredan de Animal y proporcionan una implementación concreta del método hacer_sonido.