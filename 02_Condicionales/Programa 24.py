#Calcular la edad de una persona y determinar si es mayor o menor de edad
import os, sys
from datetime import datetime
os.system ("cls")
def calcular_edad_y_mayoria():
    # Solicitar al usuario su fecha de nacimiento
    año_nacimiento = int(input("Ingresa tu año de nacimiento (AAAA): "))
    mes_nacimiento = int(input("Ingresa tu mes de nacimiento (MM): "))
    dia_nacimiento = int(input("Ingresa tu día de nacimiento (DD): "))

    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Crear un objeto datetime con la fecha de nacimiento
    fecha_nacimiento = datetime(año_nacimiento, mes_nacimiento, dia_nacimiento)

    # Calcular la edad
    edad = fecha_actual.year - fecha_nacimiento.year

    # Ajustar si aún no ha pasado el cumpleaños este año
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    # Determinar si es mayor o menor de edad
    if edad >= 18:
        return f"Tienes {edad} años. Eres mayor de edad."
    else:
        return f"Tienes {edad} años. Eres menor de edad."

# Llamar a la función y mostrar el resultado
print(calcular_edad_y_mayoria())
os.system ("pause")