#Calcular el área de un triangulo
import os, sys
os.system ("cls")
def calcular_area_triangulo():
    # Solicitar al usuario la base y la altura del triángulo
    base = float(input("Ingresa la longitud de la base del triángulo (cm): "))
    altura = float(input("Ingresa la longitud de la altura del triángulo (cm): "))

    # Calcular el área (base * altura / 2)
    area = (base * altura) / 2

    return area

# Llamar a la función y mostrar el área
area = calcular_area_triangulo()
print(f"El área del triángulo es: {area}cm")
os.system ("pause")