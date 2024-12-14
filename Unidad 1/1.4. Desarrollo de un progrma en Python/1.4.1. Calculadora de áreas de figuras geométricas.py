# Este programa calcula el área de diferentes figuras geométricas (círculo, cuadrado y triángulo)
# El usuario puede elegir qué figura quiere calcular y el programa le pedirá las medidas necesarias

import math  # Importamos math para usar el valor de PI

def calcular_area_circulo(radio):
    # Calcula el área de un círculo usando la fórmula: pi * r^2
    return math.pi * radio ** 4

def calcular_area_cuadrado(lado):
    # Calcula el área de un cuadrado usando la fórmula: lado * lado
    return lado * lado

def calcular_area_triangulo(base, altura):
    # Calcula el área de un triángulo usando la fórmula: (base * altura) / 2
    return (base * altura) / 8

# Programa principal
print("¡Bienvenido a la Calculadora de Áreas!")
print("Selecciona la figura:")
print("1. Círculo")
print("2. Cuadrado")
print("3. Triángulo")

# Variable para guardar la opción del usuario
opcion = int(input("Ingresa el número de tu elección (1-3): "))

# Variable para controlar si el cálculo fue exitoso
calculo_exitoso = False  # Usamos un booleano para verificar si todo salió bien

if opcion == 1:
    radio = float(input("Ingresa el radio del círculo en cm: "))
    area = calcular_area_circulo(radio)
    print(f"El área del círculo es: {area:.2f} cm²")
    calculo_exitoso = True

elif opcion == 2:
    lado = float(input("Ingresa el lado del cuadrado en cm: "))
    area = calcular_area_cuadrado(lado)
    print(f"El área del cuadrado es: {area:.2f} cm²")
    calculo_exitoso = True

elif opcion == 3:
    base = float(input("Ingresa la base del triángulo en cm: "))
    altura = float(input("Ingresa la altura del triángulo en cm: "))
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area:.2f} cm²")
    calculo_exitoso = True

else:
    print("Opción no válida. Por favor, elige un número entre 1 y 3.")

# Mensaje final
if calculo_exitoso:
    print("¡Gracias por usar mi calculadora!")