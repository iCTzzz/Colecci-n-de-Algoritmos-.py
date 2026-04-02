#Imprimir la sumatoria de los números del 1 al 10
import os, sys
os.system ("cls")
# Usar la función sum() con range() para calcular la sumatoria
sumatoria = sum(range(1, 11))  # range(1, 11) genera números del 1 al 10

# Imprimir el resultado
print(f"La sumatoria de los números del 1 al 10 es: {sumatoria}")
os.system ("pause")