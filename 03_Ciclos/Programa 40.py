#Realizar un programa que imprima alguna tabla de multiplicar que se desee (del 1 al 10) de cualquier número.
import os, sys
os.system ("cls")
def imprimir_tabla_multiplicar():
    # Solicitar al usuario el número para la tabla de multiplicar
    numero = int(input("Ingresa el número para la tabla de multiplicar: "))

    # Imprimir la tabla de multiplicar del 1 al 10
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):  # range(1, 11) genera números del 1 al 10
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Llamar a la función para ejecutar el programa
imprimir_tabla_multiplicar()
os.system ("pause")