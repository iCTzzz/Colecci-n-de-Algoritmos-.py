#Convertir grados Fahrenheit a grados Celcius
import os, sys
os.system ("cls")
def convertir_fahrenheit_a_celsius():
    # Solicitar al usuario la temperatura en grados Fahrenheit
    fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))

    # Aplicar la fórmula de conversión
    celsius = (fahrenheit - 32) * 5 / 9

    return f"La temperatura en grados Celsius es: {celsius:.2f} °C"

# Llamar a la función y mostrar el resultado
print(convertir_fahrenheit_a_celsius())
os.system ("pause")