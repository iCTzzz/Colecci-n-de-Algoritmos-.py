#Calcular el sueldo final de un trabajador, incluyendo un bono sobre su sueldo normal, de acuerdo a su categoría:
#Categoría A, bono del 20%, Categoría B, bono del 15%, Categoría C, bono del 10%, Categoría D, bono del 5%
import os, sys
os.system ("cls")
def calcular_sueldo_final():
    # Solicitar al usuario su sueldo normal y categoría
    sueldo_normal = float(input("Ingresa tu sueldo normal: "))
    categoria = input("Ingresa tu categoría (A, B, C o D): ").upper()

    # Determinar el porcentaje de bono según la categoría
    if categoria == "A":
        bono_porcentaje = 0.20  # 20%
    elif categoria == "B":
        bono_porcentaje = 0.15  # 15%
    elif categoria == "C":
        bono_porcentaje = 0.10  # 10%
    elif categoria == "D":
        bono_porcentaje = 0.05  # 5%
    else:
        return "Categoría no válida."

    # Calcular el monto del bono
    bono_monto = sueldo_normal * bono_porcentaje

    # Calcular el sueldo final (sueldo normal + bono)
    sueldo_final = sueldo_normal + bono_monto

    return f"Tu sueldo final es: ${sueldo_final:.2f}"

# Llamar a la función y mostrar el resultado
print(calcular_sueldo_final())
os.system ("pause")