#Se realiza un censo en una población de “N” habitantes, determinar el total de hombres y el total de mujeres de dicha población.
import os, sys
os.system ("cls")
def censo_poblacion():
    # Solicitar al usuario el número de habitantes
    N = int(input("Ingresa el número de habitantes: "))

    # Inicializar contadores para hombres y mujeres
    total_hombres = 0
    total_mujeres = 0

    # Solicitar el género de cada habitante
    for i in range(1, N + 1):
        print(f"\nDatos del habitante {i}:")
        genero = input("Ingresa el género (hombre/mujer): ").lower()

        # Contar hombres y mujeres
        if genero == "hombre":
            total_hombres += 1
        elif genero == "mujer":
            total_mujeres += 1
        else:
            print("Género no válido. Se omitirá este habitante.")

    # Mostrar los totales
    return f"\nTotal de hombres: {total_hombres}\nTotal de mujeres: {total_mujeres}"

# Llamar a la función para ejecutar el programa
print(censo_poblacion())
os.system ("pause")