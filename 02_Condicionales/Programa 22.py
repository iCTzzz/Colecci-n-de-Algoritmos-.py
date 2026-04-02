#De dos números, determinar cuál es el mayor y cuál es el menor
import os, sys
os.system ("cls")
def determinar_mayor_menor():
    # Solicitar al usuario que ingrese dos números
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))

    # Determinar cuál es el mayor y cuál es el menor
    if numero1 > numero2:
        return f"El número mayor es: {numero1}\nEl número menor es: {numero2}"
    elif numero2 > numero1:
        return f"El número mayor es: {numero2}\nEl número menor es: {numero1}"
    else:
        return "Ambos números son iguales."

# Llamar a la función y mostrar el resultado
print(determinar_mayor_menor())
os.system ("pause")