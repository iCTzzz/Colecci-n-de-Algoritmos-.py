#Determinar el salario de un trabajador considerando que puede trabajar hasta 8 horas al día y que recibe un pago de $X por cada hora trabajada
import os, sys
os.system ("cls")
def calcular_salario():
    # Solicitar al usuario las horas trabajadas y el pago por hora
    horas_trabajadas = float(input("Ingresa el número de horas trabajadas: "))
    pago_por_hora = float(input("Ingresa el pago por hora: "))

    # Verificar si las horas trabajadas exceden el límite de 8 horas al día
    if horas_trabajadas > 8:
        return "Error: No se pueden trabajar más de 8 horas al día."
    else:
        # Calcular el salario (horas trabajadas * pago por hora)
        salario = horas_trabajadas * pago_por_hora
        return f"El salario del trabajador es: ${salario:.2f}"

# Llamar a la función y mostrar el salario
print(calcular_salario())
os.system ("pause")