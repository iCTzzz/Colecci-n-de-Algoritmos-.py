#Determinar el monto a pagar de un boleto tomando en cuenta que si es adulto mayor (3ra edad) solo pagará el 50%, si es adulto, paga completo y si es mayor de 6 años, no paga.
import os, sys
os.system ("cls")
def calcular_monto_boleto():
    # Solicitar al usuario la edad del pasajero y el precio del boleto
    edad = int(input("Ingresa la edad del pasajero: "))
    precio_boleto = float(input("Ingresa el precio del boleto: "))

    # Determinar el monto a pagar según la edad
    if edad >= 60:  # Adulto mayor (3ra edad)
        monto = precio_boleto * 0.5
        return f"El pasajero es adulto mayor. Monto a pagar: ${monto:.2f}"
    elif edad >= 18:  # Adulto
        return f"El pasajero es adulto. Monto a pagar: ${precio_boleto:.2f}"
    elif edad > 6:  # Menor de 6 años
        return "El pasajero es menor de 6 años. No paga."
    else:  # Menor de 6 años
        return "El pasajero es menor de 6 años. No paga."

# Llamar a la función y mostrar el resultado
print(calcular_monto_boleto())
os.system ("pause")