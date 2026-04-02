#Imprimir los números pares del 20 al 30
import os, sys
os.system ("cls")
# Usando un bucle while
i = 20
while i <= 30:
    if i % 2 == 0:  # Verificar si el número es par
        print(i)
    i += 1  # Incrementar i en 1
os.system ("pause")