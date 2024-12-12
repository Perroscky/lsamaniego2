class automovil:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print("El automovil está arrancando.")

class Coche(automovil):
    def __init__(self, marca, modelo, numero_puertas):
        super().__init__(marca, modelo)
        self.numero_puertas = numero_puertas

    def abrir_ventanas(self):
        print("Las ventanas del automovil se han abierto.")

class Moto(automovil):
    def hacer_wheelie(self):
        print("La moto está haciendo un wheelie.")

# Creando objetos
mi_coche = Coche("Peugot 206", "Corolla", 4)
mi_moto = Moto("Honda", "CBR600RR")

mi_coche.arrancar()
mi_coche.abrir_ventanas()
mi_moto.arrancar()
mi_moto.hacer_wheelie()

# EXPLICACION DEL CODIGO
# Clase base automóvil: Define los atributos y métodos comunes a todos los vehículos (marca, modelo, arrancar).
# Clases hijas Coche y Moto: Heredan de automóvil y añaden sus propias características y métodos específicos.
# Método super().__init__(): Llama al constructor de la clase padre para inicializar los atributos heredados.
