#Calcular el área de un circulo
import os, sys
import math
os.system ("cls")
def calcular_area_circulo():
    # Solicitar al usuario el radio del círculo
    radio = float(input("Ingresa el radio del círculo (cm): "))

    # Calcular el área (pi * radio^2)
    area = math.pi * (radio ** 2)

    return area

# Llamar a la función y mostrar el área
area = calcular_area_circulo()
print(f"El área del círculo es: {area:.2f}cm")
os.system ("pause")
