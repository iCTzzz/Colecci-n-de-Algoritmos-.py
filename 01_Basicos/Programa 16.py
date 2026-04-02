#Convertir dólares a pesos mexicanos considerando la tasa de cambio de $1 dólar = $18 pesos
import os, sys
os.system ("cls")
def convertir_dolares_a_pesos():
    # Solicitar al usuario la cantidad en dólares
    dolares = float(input("Ingresa la cantidad en dólares (USD): "))

    # Tasa de cambio: 1 USD = 18 MXN
    tasa_cambio = 18

    # Calcular la cantidad en pesos mexicanos
    pesos = dolares * tasa_cambio

    return f"La cantidad en pesos mexicanos es: ${pesos:.2f} MXN"

# Llamar a la función y mostrar el resultado
print(convertir_dolares_a_pesos())
os.system ("pause")