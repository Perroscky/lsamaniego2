class Dia:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, nueva_temperatura):
        self.__temperatura = nueva_temperatura

class Semana:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, dia):
        self.dias.append(dia)

    def calcular_promedio(self):
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias)

# Crear una semana
semana = Semana()

# Agregar días a la semana
for dia in range(1, 8):
    temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
    nuevo_dia = Dia(temperatura)
    semana.agregar_dia(nuevo_dia)

# Calcular y mostrar el promedio
promedio = semana.calcular_promedio()
print(f"El promedio de temperatura semanal es: {promedio:.2f} °C")35