#Imprimir los números pares del 20 al 30
import os, sys
os.system ("cls")
# Usando un bucle for
for i in range(20, 31):  # range(20, 31) genera números del 20 al 30
    if i % 2 == 0:  # Verificar si el número es par
        print(i)
os.system ("pause")