#Calcular el área de un cuadrado
import os, sys
os.system ("cls")
def calcular_area_cuadrado():
    # Solicitar al usuario la longitud del lado del cuadrado
    lado = float(input("Ingresa la longitud del lado del cuadrado (cm): "))

    # Calcular el área (lado * lado)
    area = lado ** 2

    return area

# Llamar a la función y mostrar el área
area = calcular_area_cuadrado()
print(f"El área del cuadrado es: {area}cm")
os.system ("pause")