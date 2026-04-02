#Determinar el sueldo final de un trabajador de acuerdo al siguiente criterio:
#Sueldo > 5,000 y < 10,000: ISR= 5%, Sueldo >= 10,000 y < 15,000: ISR= 10%, Sueldo >= 15,000 y < 20,000: ISR= 12%, Sueldo >= 20,000: ISR= 15%
import os, sys
os.system ("cls")
def calcular_sueldo_final():
    # Solicitar al usuario su sueldo bruto
    sueldo_bruto = float(input("Ingresa tu sueldo bruto: "))

    # Determinar el porcentaje de ISR según el rango del sueldo
    if 5000 < sueldo_bruto < 10000:
        isr_porcentaje = 0.05  # 5%
    elif 10000 <= sueldo_bruto < 15000:
        isr_porcentaje = 0.10  # 10%
    elif 15000 <= sueldo_bruto < 20000:
        isr_porcentaje = 0.12  # 12%
    elif sueldo_bruto >= 20000:
        isr_porcentaje = 0.15  # 15%
    else:
        isr_porcentaje = 0  # No aplica ISR

    # Calcular el monto del ISR
    isr_monto = sueldo_bruto * isr_porcentaje

    # Calcular el sueldo final (sueldo bruto - ISR)
    sueldo_final = sueldo_bruto - isr_monto

    return f"Tu sueldo final es: ${sueldo_final:.2f}"

# Llamar a la función y mostrar el resultado
print(calcular_sueldo_final())
os.system ("pause")