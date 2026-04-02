#Calcular el precio final de un producto o articulo, al cual se le aplica un IVA del X%
import os, sys
os.system ("cls")
def calcular_precio_final():
    # Solicitar al usuario el precio base y el porcentaje de IVA
    precio_base = float(input("Ingresa el precio base del producto: "))
    porcentaje_iva = float(input("Ingresa el porcentaje de IVA (X%): "))

    # Calcular el monto del IVA
    iva = (precio_base * porcentaje_iva) / 100

    # Calcular el precio final (precio base + IVA)
    precio_final = precio_base + iva

    return f"El precio final del producto es: ${precio_final:.2f}"

# Llamar a la función y mostrar el precio final
print(calcular_precio_final())
os.system ("pause")