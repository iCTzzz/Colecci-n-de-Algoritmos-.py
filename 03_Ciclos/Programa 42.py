#Realizar un programa que imprima la sumatoria de los números pares desde 2 hasta “N”
import os, sys
os.system ("cls")
def sumatoria_numeros_pares():
    # Solicitar al usuario el valor de N
    N = int(input("Ingresa el valor de N: "))

    # Inicializar una variable para almacenar la sumatoria
    sumatoria = 0

    # Iterar sobre los números pares desde 2 hasta N
    for i in range(2, N + 1, 2):  # El tercer parámetro (2) indica el paso
        sumatoria += i  # Sumar el número par a la sumatoria

    # Mostrar la sumatoria
    return f"La sumatoria de los números pares desde 2 hasta {N} es: {sumatoria}"

# Llamar a la función para ejecutar el programa
print(sumatoria_numeros_pares())
os.system ("pause")