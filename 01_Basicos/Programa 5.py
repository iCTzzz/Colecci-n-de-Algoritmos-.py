#Calcular la edad de una persona
from datetime import datetime
import os, sys
os.system ("cls")
def calcular_edad():
    # Solicitar al usuario que ingrese su fecha de nacimiento
    año = int(input("Ingresa tu año de nacimiento (AAAA): "))
    mes = int(input("Ingresa tu mes de nacimiento (MM): "))
    dia = int(input("Ingresa tu día de nacimiento (DD): "))

    # Crear un objeto datetime con la fecha de nacimiento
    fecha_nacimiento = datetime(año, mes, dia)

    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Calcular la edad
    edad = fecha_actual.year - fecha_nacimiento.year

    # Ajustar si aún no ha pasado el cumpleaños este año
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    return edad

# Llamar a la función y mostrar la edad
edad = calcular_edad()
print(f"Tu edad es: {edad} años")
os.system ("pause")