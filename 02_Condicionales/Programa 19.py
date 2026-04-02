#Convertir grados Celsius a grados Fahrenheit
import os, sys
os.system ("cls")
def convertir_celsius_a_fahrenheit():
    # Solicitar al usuario la temperatura en grados Celsius
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))

    # Aplicar la fórmula de conversión
    fahrenheit = (celsius * 9 / 5) + 32

    return f"La temperatura en grados Fahrenheit es: {fahrenheit:.2f} °F"

# Llamar a la función y mostrar el resultado
print(convertir_celsius_a_fahrenheit())
os.system ("pause")