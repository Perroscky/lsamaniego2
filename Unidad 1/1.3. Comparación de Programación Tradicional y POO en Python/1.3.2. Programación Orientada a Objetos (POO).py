class Dia:
    """
    Representa un día y almacena su temperatura.
    """
    def __init__(self, temperatura):
        """
        Inicializa un objeto Dia con una temperatura dada.

        Args:
            temperatura (float): La temperatura del día.
        """
        self.__temperatura = temperatura

    def get_temperatura(self):
        """
        Obtiene la temperatura del día.

        Returns:
            float: La temperatura del día.
        """
        return self.__temperatura

    def set_temperatura(self, nueva_temperatura):
        """
        Establece una nueva temperatura para el día.

        Args:
            nueva_temperatura (float): La nueva temperatura.
        """
        self.__temperatura = nueva_temperatura

class Semana:
    """
    Representa una semana y contiene una lista de días.
    """
    def __init__(self):
        """
        Inicializa una semana vacía.
        """
        self.dias = []

    def agregar_dia(self, dia):
        """
        Agrega un día a la semana.

        Args:
            dia (Dia): Un objeto de la clase Dia.
        """
        self.dias.append(dia)

    def calcular_promedio(self):
        """
        Calcula el promedio de las temperaturas de la semana.

        Returns:
            float: El promedio de las temperaturas.
        """
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
print(f"El promedio de temperatura semanal es: {promedio:.2f} °C")