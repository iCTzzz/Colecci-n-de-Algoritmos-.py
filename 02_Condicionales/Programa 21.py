#Determinar si un número es positivo o negativo
import os, sys
os.system ("cls")
def determinar_signo():
    # Solicitar al usuario que ingrese un número
    numero = float(input("Ingresa un número: "))

    # Determinar si es positivo, negativo o cero
    if numero > 0:
        return "El número es positivo."
    elif numero < 0:
        return "El número es negativo."
    else:
        return "El número es cero (no es positivo ni negativo)."

# Llamar a la función y mostrar el resultado
print(determinar_signo())
os.system ("pause")