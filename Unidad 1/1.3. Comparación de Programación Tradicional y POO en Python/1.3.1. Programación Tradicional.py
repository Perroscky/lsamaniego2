def ingresar_temperaturas_semanales():
    temperaturas = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

temperaturas_semana = ingresar_temperaturas_semanales()
promedio_semanal = calcular_promedio(temperaturas_semana)

print(f"El promedio de temperatura semanal es: {promedio_semanal:.2f} °C")