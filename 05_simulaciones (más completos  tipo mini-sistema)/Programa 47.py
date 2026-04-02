#Tomando en cuenta un grupo escolar de "N" alumnos, calcular el promedio general de calificaciones de todo del grupo, considerando que se cursaron "Y" cantidad de materias durante el semestre.
import os, sys
os.system ("cls")
def calcular_promedio_general():
    # Solicitar al usuario el número de alumnos y materias
    N = int(input("Ingresa el número de alumnos: "))
    Y = int(input("Ingresa el número de materias: "))

    # Inicializar una variable para almacenar la suma de los promedios de los alumnos
    suma_promedios = 0

    # Solicitar las calificaciones de cada alumno
    for i in range(1, N + 1):
        print(f"\nDatos del alumno {i}:")
        suma_calificaciones = 0

        # Solicitar las calificaciones de cada materia
        for j in range(1, Y + 1):
            calificacion = float(input(f"Ingresa la calificación de la materia {j}: "))
            suma_calificaciones += calificacion

        # Calcular el promedio del alumno
        promedio_alumno = suma_calificaciones / Y
        suma_promedios += promedio_alumno

    # Calcular el promedio general del grupo
    promedio_general = suma_promedios / N

    # Mostrar el promedio general
    return f"\nEl promedio general del grupo es: {promedio_general:.2f}"

# Llamar a la función para ejecutar el programa
print(calcular_promedio_general())
os.system ("pause")