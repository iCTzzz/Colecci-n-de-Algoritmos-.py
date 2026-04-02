#Calcular el precio final de un producto o articulo, al cual se le aplica un IVA del X% y también se le aplica un descuento del Y%
import os, sys
os.system ("cls")
def calcular_precio_final():
    # Solicitar al usuario el precio base, el porcentaje de IVA y el porcentaje de descuento
    precio_base = float(input("Ingresa el precio base del producto: "))
    porcentaje_iva = float(input("Ingresa el porcentaje de IVA (X%): "))
    porcentaje_descuento = float(input("Ingresa el porcentaje de descuento (Y%): "))

    # Calcular el monto del descuento
    descuento = (precio_base * porcentaje_descuento) / 100

    # Calcular el precio con descuento
    precio_con_descuento = precio_base - descuento

    # Calcular el monto del IVA sobre el precio con descuento
    iva = (precio_con_descuento * porcentaje_iva) / 100

    # Calcular el precio final (precio con descuento + IVA)
    precio_final = precio_con_descuento + iva

    return f"El precio final del producto es: ${precio_final:.2f}"

# Llamar a la función y mostrar el precio final
print(calcular_precio_final())
os.system ("pause")