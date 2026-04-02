#Se realiza un censo en un población de "N" habitantes, determinar el total de hombres mayores de edad y hombres menores de edad, así como el total de mujeres mayores de edad y mujeres menores de edad.
import os, sys
os.system ("cls")
def censo_poblacion():
    # Solicitar al usuario el número de habitantes
    N = int(input("Ingresa el número de habitantes: "))

    # Inicializar contadores para cada categoría
    hombres_mayores = 0
    hombres_menores = 0
    mujeres_mayores = 0
    mujeres_menores = 0

    # Solicitar el género y la edad de cada habitante
    for i in range(1, N + 1):
        print(f"\nDatos del habitante {i}:")
        genero = input("Ingresa el género (hombre/mujer): ").lower()
        edad = int(input("Ingresa la edad: "))

        # Clasificar al habitante según género y edad
        if genero == "hombre":
            if edad >= 18:
                hombres_mayores += 1
            else:
                hombres_menores += 1
        elif genero == "mujer":
            if edad >= 18:
                mujeres_mayores += 1
            else:
                mujeres_menores += 1
        else:
            print("Género no válido. Se omitirá este habitante.")

    # Mostrar los totales
    return (f"\nTotal de hombres mayores de edad: {hombres_mayores}"
            f"\nTotal de hombres menores de edad: {hombres_menores}"
            f"\nTotal de mujeres mayores de edad: {mujeres_mayores}"
            f"\nTotal de mujeres menores de edad: {mujeres_menores}")

# Llamar a la función para ejecutar el programa
print(censo_poblacion())
os.system ("pause")