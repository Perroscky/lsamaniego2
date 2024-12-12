class Coche:
    def __init__(self, marca, modelo, color):
        self.__marca = marca  # Atributo privado
        self.__modelo = modelo
        self.__color = color
        self.__velocidad = 0

    def acelerar(self, incremento):
        self.__velocidad += incremento
        print("Acelerando... Velocidad actual:", self.__velocidad)

    def frenar(self, decremento):
        self.__velocidad -= decremento
        print("Frenando... Velocidad actual:", self.__velocidad)

    def get_marca(self):  # Método getter
        return self.__marca

# Crear un objeto de la clase Coche
mi_coche = Coche("Peugot 206", "Corolla", "Rojo")

# Acceder a los atributos y métodos públicos
print(mi_coche.get_marca())  # Imprime: Peugot 20
mi_coche.acelerar(100)
mi_coche.frenar(65)
# EXPLICACION DEL CODIGO
# Atributos privados: Las propiedades que se encuentran precedidas por dos guiones bajos (__) se consideran privadas y
# no pueden ser accesibles directamente desde el exterior de la clase. Esto resguarda los datos internos de la clase y
# previene cambios indeseables.
# Métodos:: Los procedimientos de aceleración y frenado alteran la condición interna del objeto (la velocidad),
# pero no presentan de manera directa el atributo privado __velocidad.
# Métodos getter: El procedimiento get_marca ofrece un método regulado para acceder al valor del
#  atributo privado __marca.
# Encapsulación: El objetivo de la encapsulación es ocultar los detalles internos del funcionamiento del vehículo
# (como se determina la velocidad, etc.) y ofrecer una interfaz pública (métodos) para interactuar con el objeto.