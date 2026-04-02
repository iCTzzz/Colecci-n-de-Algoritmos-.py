#Realizar un programa que calcule e imprima el promedio de estatura y peso (kg) de un grupo de “N” alumnos
import os, sys
os.system ("cls")
def calcular_promedio_estatura_peso():
    # Solicitar al usuario el número de alumnos
    N = int(input("Ingresa el número de alumnos: "))

    # Inicializar variables para almacenar las sumas
    suma_estaturas = 0
    suma_pesos = 0

    # Solicitar la estatura y el peso de cada alumno
    for i in range(1, N + 1):
        print(f"\nDatos del alumno {i}:")
        estatura = float(input("Ingresa la estatura (en metros): "))
        peso = float(input("Ingresa el peso (en kg): "))

        # Sumar la estatura y el peso a las sumas totales
        suma_estaturas += estatura
        suma_pesos += peso

    # Calcular los promedios
    promedio_estatura = suma_estaturas / N
    promedio_peso = suma_pesos / N

    # Mostrar los promedios
    return f"\nPromedio de estatura: {promedio_estatura:.2f} metros\nPromedio de peso: {promedio_peso:.2f} kg"

# Llamar a la función para ejecutar el programa
print(calcular_promedio_estatura_peso())
os.system ("pause")