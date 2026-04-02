#Con base a la calificación obtenida en una materia, determinar si el alumno aprobó o reprobó
import os, sys
os.system ("cls")
def determinar_aprobacion():
    # Solicitar al usuario la calificación obtenida y el criterio de aprobación
    calificacion = float(input("Ingresa la calificación obtenida: "))
    criterio_aprobacion = float(input("Ingresa el criterio de aprobación: "))

    # Determinar si el alumno aprobó o reprobó
    if calificacion >= criterio_aprobacion:
        return "El alumno aprobó."
    else:
        return "El alumno reprobó."

# Llamar a la función y mostrar el resultado
print(determinar_aprobacion())
os.system ("pause")