#Calcular el área de un rectángulo
import os, sys
os.system ("cls")
def calcular_area_rectangulo():
    # Solicitar al usuario la base y la altura del rectángulo
    base = float(input("Ingresa la longitud de la base del rectángulo (cm): "))
    altura = float(input("Ingresa la longitud de la altura del rectángulo (cm): "))

    # Calcular el área (base * altura)
    area = base * altura

    return area

# Llamar a la función y mostrar el área
area = calcular_area_rectangulo()
print(f"El área del rectángulo es: {area}cm")
os.system ("pause")