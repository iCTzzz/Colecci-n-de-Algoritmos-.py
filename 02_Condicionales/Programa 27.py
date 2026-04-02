#Con base a la tabla del IMC y a la formula correspondiente para obtenerla, determinar el estado de salud de una persona
import os, sys
os.system ("cls")
def calcular_imc():
    # Solicitar al usuario su peso y altura
    peso = float(input("Ingresa tu peso en kilogramos (kg): "))
    altura = float(input("Ingresa tu altura en metros (m): "))

    # Calcular el IMC
    imc = peso / (altura ** 2)

    # Determinar el estado de salud según el IMC
    if imc < 18.5:
        estado = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        estado = "Peso normal"
    elif 25 <= imc < 29.9:
        estado = "Sobrepeso"
    else:
        estado = "Obesidad"

    return f"Tu IMC es: {imc:.2f}\nEstado de salud: {estado}"

# Llamar a la función y mostrar el resultado
print(calcular_imc())
os.system ("pause")