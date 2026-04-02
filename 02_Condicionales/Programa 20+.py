#Usuario pone la velocidad y el tiempo
import os, sys
os.system ("cls")
def calcular_distancia():
    # Solicitar al usuario la velocidad y el tiempo
    velocidad = float(input("Ingresa la velocidad (Km/H): "))
    tiempo_minutos = float(input("Ingresa el tiempo (minutos): "))

    # Convertir el tiempo de minutos a horas
    tiempo_horas = tiempo_minutos / 60

    # Calcular la distancia (velocidad * tiempo)
    distancia = velocidad * tiempo_horas

    return f"La distancia recorrida es: {distancia:.2f} Km"

# Llamar a la función y mostrar el resultado
print(calcular_distancia())
os.system ("pause")