#Calcular el precio final de un producto o articulo, al cual se le aplica un descuento del X%
import os, sys
os.system ("cls")
def calcular_precio_final():
    # Solicitar al usuario el precio base y el porcentaje de descuento
    precio_base = float(input("Ingresa el precio base del producto: "))
    porcentaje_descuento = float(input("Ingresa el porcentaje de descuento (X%): "))

    # Calcular el monto del descuento
    descuento = (precio_base * porcentaje_descuento) / 100

    # Calcular el precio final (precio base - descuento)
    precio_final = precio_base - descuento

    return f"El precio final del producto es: ${precio_final:.2f}"

# Llamar a la función y mostrar el precio final
print(calcular_precio_final())
os.system ("pause")