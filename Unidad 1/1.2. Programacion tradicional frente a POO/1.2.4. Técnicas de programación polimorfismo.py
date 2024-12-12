class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        import math
        return math.pi * self.radio**2

    # EXPLICACION DEL CODIGO
    # El Cuadrado: Hereda de Figura y agrega atributos específicos para un rectángulo (base y altura). Redefine
    # el método área () para calcular el área de un rectángulo.
    # El Triangulo: También hereda de Figura y agrega el atributo radio. Redefine area() para calcular el área de un
    # círculo, utilizando la constante pi del módulo math.