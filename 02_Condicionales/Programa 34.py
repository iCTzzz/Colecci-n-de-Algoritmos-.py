#Calcular el total a pagar por un boleto en una línea de transporte, de acuerdo a los siguientes tarifas sobre su costo normal, dependiendo del tipo de pasajero:
#Niños menores de 8 años= $0, Estudiante con credencial= 40% descuento, Anciano con INAPAM= 55% descuento, Adulto normal= 0% descuento
import os, sys
os.system ("cls")
def calcular_total_boleto():
    # Solicitar al usuario el costo normal del boleto y el tipo de pasajero
    costo_normal = float(input("Ingresa el costo normal del boleto: "))
    tipo_pasajero = input("Ingresa el tipo de pasajero (niño, estudiante, anciano, adulto): ").lower()

    # Determinar el descuento según el tipo de pasajero
    if tipo_pasajero == "niño":
        descuento_porcentaje = 1.00  # 100% de descuento (boleto gratuito)
    elif tipo_pasajero == "estudiante":
        descuento_porcentaje = 0.40  # 40% de descuento
    elif tipo_pasajero == "anciano":
        descuento_porcentaje = 0.55  # 55% de descuento
    elif tipo_pasajero == "adulto":
        descuento_porcentaje = 0.00  # 0% de descuento
    else:
        return "Tipo de pasajero no válido."

    # Calcular el monto del descuento
    descuento_monto = costo_normal * descuento_porcentaje

    # Calcular el total a pagar (costo normal - descuento)
    total_pagar = costo_normal - descuento_monto

    return f"El total a pagar es: ${total_pagar:.2f}"

# Llamar a la función y mostrar el resultado
print(calcular_total_boleto())
os.system ("pause")