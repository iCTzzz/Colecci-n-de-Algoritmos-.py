#Realizar un programa para calcular el promedio general de un alumno que cursó "n" materias en el semestre.
import os, sys
os.system ("cls")
def calcular_promedio():
    # Solicitar al usuario el número de materias cursadas
    n = int(input("Ingresa el número de materias cursadas: "))

    # Inicializar una variable para almacenar la suma de las calificaciones
    suma_calificaciones = 0

    # Solicitar las calificaciones de cada materia
    for i in range(1, n + 1):
        calificacion = float(input(f"Ingresa la calificación de la materia {i}: "))
        suma_calificaciones += calificacion  # Sumar la calificación al total

    # Calcular el promedio
    promedio = suma_calificaciones / n

    # Mostrar el promedio general
    return f"El promedio general es: {promedio:.2f}"

# Llamar a la función para ejecutar el programa
print(calcular_promedio())
os.system ("pause")