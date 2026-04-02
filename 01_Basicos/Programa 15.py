#Convertir pesos mexicanos a dólares considerando la tasa de cambio de $18 pesos = $1 dólar
import os, sys
os.system ("cls")
def convertir_pesos_a_dolares():
    # Solicitar al usuario la cantidad en pesos mexicanos
    pesos = float(input("Ingresa la cantidad en pesos mexicanos (MXN): "))

    # Tasa de cambio: 18 MXN = 1 USD
    tasa_cambio = 18

    # Calcular la cantidad en dólares
    dolares = pesos / tasa_cambio

    return f"La cantidad en dólares es: ${dolares:.2f} USD"

# Llamar a la función y mostrar el resultado
print(convertir_pesos_a_dolares())
os.system ("pause")