#código para parciales con pesos diferentes:
import os, sys
os.system ("cls")
def calcular_calificacion_final():
    # Solicitar las calificaciones de los 3 parciales
    parcial1 = float(input("Ingresa la calificación del primer parcial: "))
    parcial2 = float(input("Ingresa la calificación del segundo parcial: "))
    parcial3 = float(input("Ingresa la calificación del tercer parcial: "))

    # Solicitar los pesos de cada parcial (deben sumar 100%)
    peso1 = float(input("Ingresa el peso del primer parcial (%): "))
    peso2 = float(input("Ingresa el peso del segundo parcial (%): "))
    peso3 = float(input("Ingresa el peso del tercer parcial (%): "))

    # Verificar que los pesos sumen 100%
    if (peso1 + peso2 + peso3) != 100:
        return "Error: Los pesos deben sumar 100%."

    # Calcular la calificación final (ponderada)
    calificacion_final = (parcial1 * peso1 + parcial2 * peso2 + parcial3 * peso3) / 100

    return f"La calificación final es: {calificacion_final:.2f}"

# Llamar a la función y mostrar el resultado
print(calcular_calificacion_final())
os.system ("pause")