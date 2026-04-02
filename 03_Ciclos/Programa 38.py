#Imprimir números impares del 1 al 50
import os, sys
os.system ("cls")
# Usando un bucle for
for i in range(1, 51):  # range(1, 51) genera números del 1 al 50
    if i % 2 != 0:  # Verificar si el número es impar
        print(i)
os.system ("pause")