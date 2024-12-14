def ingresar_temperaturas_semanales():
    """
    Esta función solicita al usuario que ingrese las temperaturas de una semana y
    las almacena en una lista.

    Returns:
        list: Una lista que contiene las temperaturas ingresadas.
    """
    temperaturas = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.

    Args:
        temperaturas (list): Una lista de temperaturas.

    Returns:
        float: El promedio de las temperaturas.
    """
    return sum(temperaturas) / len(temperaturas)

# Bloque principal del programa
temperaturas_semana = ingresar_temperaturas_semanales()
promedio_semanal = calcular_promedio(temperaturas_semana)

print(f"El promedio de temperatura semanal es: {promedio_semanal:.2f} °C")