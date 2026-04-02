#Calcular el total a pagar por un producto al que se le aplica un descuento sobre su precio normal, de acuerdo al color de su etiqueta:
#Etiqueta roja, descuento del 35%, Etiqueta azul, descuento del 25%, Etiqueta verde, descuento del 15%, 4.Etiqueta amarilla, descuento del 5%
import os, sys
os.system ("cls")
def calcular_total_pagar():
    # Solicitar al usuario el precio normal y el color de la etiqueta
    precio_normal = float(input("Ingresa el precio normal del producto: "))
    color_etiqueta = input("Ingresa el color de la etiqueta (roja, azul, verde o amarilla): ").lower()

    # Determinar el porcentaje de descuento según el color de la etiqueta
    if color_etiqueta == "roja":
        descuento_porcentaje = 0.35  # 35%
    elif color_etiqueta == "azul":
        descuento_porcentaje = 0.25  # 25%
    elif color_etiqueta == "verde":
        descuento_porcentaje = 0.15  # 15%
    elif color_etiqueta == "amarilla":
        descuento_porcentaje = 0.05  # 5%
    else:
        return "Color de etiqueta no válido."

    # Calcular el monto del descuento
    descuento_monto = precio_normal * descuento_porcentaje

    # Calcular el total a pagar (precio normal - descuento)
    total_pagar = precio_normal - descuento_monto

    return f"El total a pagar es: ${total_pagar:.2f}"

# Llamar a la función y mostrar el resultado
print(calcular_total_pagar())
os.system ("pause")