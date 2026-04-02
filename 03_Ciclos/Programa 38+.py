#Imprimir números impares del 1 al 50
import os, sys
os.system ("cls")
# Usando un bucle while
i = 1
while i <= 50:
    if i % 2 != 0:  # Verificar si el número es impar
        print(i)
    i += 1  # Incrementar i en 1
os.system ("pause")