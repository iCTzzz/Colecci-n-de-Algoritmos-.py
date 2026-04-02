#Determinar el tipo de pasajero en una aerolínea, de acuerdo al costo del boleto:
#3ra Clase = Costo del boleto <= $1,000, 2da Clase = Costo del boleto > $1,000 y <= $2,000, 1ra Clase = Costo del boleto > $2,000 y <= $3,000, VIP = Costo del boleto > $3,000
import os, sys
os.system ("cls")
def determinar_tipo_pasajero():
    # Solicitar al usuario el costo del boleto
    costo_boleto = float(input("Ingresa el costo del boleto: "))

    # Determinar el tipo de pasajero según el costo del boleto
    if costo_boleto <= 1000:
        tipo_pasajero = "3ra Clase"
    elif 1000 < costo_boleto <= 2000:
        tipo_pasajero = "2da Clase"
    elif 2000 < costo_boleto <= 3000:
        tipo_pasajero = "1ra Clase"
    else:  # Costo del boleto > 3000
        tipo_pasajero = "VIP"

    return f"El tipo de pasajero es: {tipo_pasajero}"

# Llamar a la función y mostrar el resultado
print(determinar_tipo_pasajero())
os.system ("pause")