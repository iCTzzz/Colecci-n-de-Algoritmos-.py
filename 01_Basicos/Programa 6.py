#Calcular el cambio a recibir después de una compra
import os, sys
os.system ("cls")
def calcular_cambio():
    # Solicitar el monto total de la compra
    total_compra = float(input("Ingresa el monto total de la compra: "))

    # Solicitar el monto con el que el cliente paga
    monto_pagado = float(input("Ingresa el monto con el que se paga: "))

    # Calcular el cambio
    cambio = monto_pagado - total_compra

    # Verificar si el monto pagado es suficiente
    if cambio < 0:
        return "El monto pagado no es suficiente para cubrir la compra."
    else:
        return f"El cambio a recibir es: {cambio:.2f}"

# Llamar a la función y mostrar el cambio
print(calcular_cambio())
os.system ("pause")