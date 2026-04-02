#Imprimir la sumatoria de los números del 1 al 10
import os, sys
os.system ("cls")
# Inicializar una variable para almacenar la suma
sumatoria = 0

# Usar un bucle for para sumar los números del 1 al 10
for i in range(1, 11):  # range(1, 11) genera números del 1 al 10
    sumatoria += i  # Sumar el valor de i a la sumatoria

# Imprimir el resultado
print(f"La sumatoria de los números del 1 al 10 es: {sumatoria}")
os.system ("pause")