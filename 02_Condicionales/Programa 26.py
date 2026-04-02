#Un cliente compra una determinada cantidad de artículos, para lo cual recibirá un descuento en el monto total de lo comprado con base al siguiente criterio:
#Menos de 10 artículos = Descuento 5%, De 10 a 19 artículos = Descuento 10%, De 20 a 29 artículos = Descuento 15%, Más de 30 artículos = Descuento del 25%
#Calcular el monto total a pagar por los artículos comprados después de aplicar el descuento que corresponda
import os, sys
os.system ("cls")
def calcular_monto_total():
    # Solicitar al usuario la cantidad de artículos y el precio unitario
    cantidad = int(input("Ingresa la cantidad de artículos comprados: "))
    precio_unitario = float(input("Ingresa el precio unitario de cada artículo: "))

    # Calcular el monto total sin descuento
    monto_sin_descuento = cantidad * precio_unitario

    # Aplicar el descuento según la cantidad de artículos
    if cantidad < 10:
        descuento = 0.05  # 5%
    elif 10 <= cantidad <= 19:
        descuento = 0.10  # 10%
    elif 20 <= cantidad <= 29:
        descuento = 0.15  # 15%
    else:  # Más de 30 artículos
        descuento = 0.25  # 25%

    # Calcular el monto con descuento
    monto_con_descuento = monto_sin_descuento * (1 - descuento)

    return f"Monto total a pagar (con descuento): ${monto_con_descuento:.2f}"

# Llamar a la función y mostrar el resultado
print(calcular_monto_total())
os.system ("pause")