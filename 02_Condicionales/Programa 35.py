#Realizar el tipo de operación aritmética básica para 2 números introducidos, y mostrar el resultado, de acuerdo a las siguientes opciones
#Suma, Resta, Multiplicación, División
import os, sys
os.system ("cls")
def realizar_operacion():
    # Solicitar al usuario dos números
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    # Solicitar al usuario la operación a realizar
    operacion = input("Ingresa la operación (suma, resta, multiplicación, división): ").lower()

    # Realizar la operación seleccionada
    if operacion == "suma":
        resultado = numero1 + numero2
    elif operacion == "resta":
        resultado = numero1 - numero2
    elif operacion == "multiplicación":
        resultado = numero1 * numero2
    elif operacion == "división":
        if numero2 == 0:
            return "Error: No se puede dividir entre cero."
        resultado = numero1 / numero2
    else:
        return "Operación no válida."

    return f"El resultado de la {operacion} es: {resultado:.2f}"

# Llamar a la función y mostrar el resultado
print(realizar_operacion())
os.system("pause")