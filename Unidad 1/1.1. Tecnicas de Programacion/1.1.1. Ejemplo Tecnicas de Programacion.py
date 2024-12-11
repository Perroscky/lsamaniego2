import random

# Clase para los guerreros Saiyajin
# Cada guerrero tiene atributos: nombre, ataque, defensa y vida.
class GuerreroSaiyajin:
    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
# Metodo: atacar: Reduce la vida del oponente en función del ataque y defensa, atacar: Reduce la vida del oponente en función del ataque y defensa

    def atacar(self, otro):
        # Cálculo del daño: ataque - defensa del oponente
        daño = max(0, self.ataque - otro.defensa + random.randint(-5, 5))  # Variación aleatoria
        otro.vida -= daño
        print(f"{self.nombre} ataca a {otro.nombre} causando {daño} de daño.")

    def mostrar_estado(self):
        print(f"{self.nombre} - Vida: {self.vida}, Ataque: {self.ataque}, Defensa: {self.defensa}")

# Clase para el combate: Son dos guerreros y maneja el flujo del combate, Alterna turnos hasta que la vida de uno llegue a 0.

class CombateSaiyajin:
    def __init__(self, saiyajin1, saiyajin2):
        self.saiyajin1 = saiyajin1
        self.saiyajin2 = saiyajin2

    def iniciar(self):
        print("¡El combate Saiyajin comienza!")
        # Turnos alternos hasta que uno de los dos pierda
        while self.saiyajin1.vida > 0 and self.saiyajin2.vida > 0:
            self.saiyajin1.atacar(self.saiyajin2)
            if self.saiyajin2.vida <= 0:
                print(f"¡{self.saiyajin1.nombre} gana el combate!")
                break

            self.saiyajin2.atacar(self.saiyajin1)
            if self.saiyajin1.vida <= 0:
                print(f"¡{self.saiyajin2.nombre} gana el combate!")
                break

            # Mostrar estados después de cada ronda
            self.saiyajin1.mostrar_estado()
            self.saiyajin2.mostrar_estado()

# Crear guerreros Saiyajin
goku = GuerreroSaiyajin("Goku", ataque=25, defensa=20, vida=100)
vegeta = GuerreroSaiyajin("Vegeta", ataque=23, defensa=18, vida=90)

# Crear y comenzar el combate
combate = CombateSaiyajin(goku, vegeta)
combate.iniciar()

# Se usa una ligera variación aleatoria en el daño (random.randint(-5, 5)) para hacer la pelea más impredecible.
# Los guerreros atacan alternadamente hasta que uno de ellos gane.
