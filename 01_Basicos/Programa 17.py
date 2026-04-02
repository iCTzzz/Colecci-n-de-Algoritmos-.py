#Calcular la calificación final obtenida por un alumno en una asignatura “X”, considerando 3 parciales durante el semestre
import os, sys
os.system ("cls")
def calcular_calificacion_final():
    # Solicitar las calificaciones de los 3 parciales
    parcial1 = float(input("Ingresa la calificación del primer parcial: "))
    parcial2 = float(input("Ingresa la calificación del segundo parcial: "))
    parcial3 = float(input("Ingresa la calificación del tercer parcial: "))

    # Calcular el promedio (mismo peso para los 3 parciales)
    calificacion_final = (parcial1 + parcial2 + parcial3) / 3

    return f"La calificación final es: {calificacion_final:.2f}"

# Llamar a la función y mostrar el resultado
print(calcular_calificacion_final())
os.system ("pause")