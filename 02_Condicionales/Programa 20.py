#Calcular la velocidad a la que circula un automóvil que recorre una distancia de 203 Km/H en un tiempo de 98 Min
import os, sys
os.system ("cls")
def calcular_velocidad():
    # Datos proporcionados
    distancia = 203  # en kilómetros
    tiempo_minutos = 98  # en minutos

    # Convertir el tiempo de minutos a horas
    tiempo_horas = tiempo_minutos / 60

    # Calcular la velocidad (distancia / tiempo)
    velocidad = distancia / tiempo_horas

    return f"La velocidad del automóvil es: {velocidad:.2f} Km/H"

# Llamar a la función y mostrar el resultado
print(calcular_velocidad())
os.system ("pause")