import os

def censo_for():
    os.system("cls")
    N = int(input("Ingresa el número de habitantes: "))
    total_hombres = 0
    total_mujeres = 0

    for i in range(1, N + 1):
        print(f"\nDatos del habitante {i}:")
        genero = input("Ingresa el género (hombre/mujer): ").lower()

        if genero == "hombre":
            total_hombres += 1
        elif genero == "mujer":
            total_mujeres += 1
        else:
            print("Género no válido. Se omitirá este habitante.")

    print(f"\nTotal de hombres: {total_hombres}")
    print(f"Total de mujeres: {total_mujeres}")

def censo_while():
    os.system("cls")
    N = int(input("Ingresa el número de habitantes: "))
    total_hombres = 0
    total_mujeres = 0
    i = 1

    while i <= N:
        print(f"\nDatos del habitante {i}:")
        genero = input("Ingresa el género (hombre/mujer): ").lower()

        if genero == "hombre":
            total_hombres += 1
        elif genero == "mujer":
            total_mujeres += 1
        else:
            print("Género no válido. Se omitirá este habitante.")
        i += 1

    print(f"\nTotal de hombres: {total_hombres}")
    print(f"Total de mujeres: {total_mujeres}")

def censo_repeat():
    os.system("cls")
    N = int(input("Ingresa el número de habitantes: "))
    total_hombres = 0
    total_mujeres = 0
    i = 1

    while True:
        print(f"\nDatos del habitante {i}:")
        genero = input("Ingresa el género (hombre/mujer): ").lower()

        if genero == "hombre":
            total_hombres += 1
        elif genero == "mujer":
            total_mujeres += 1
        else:
            print("Género no válido. Se omitirá este habitante.")

        i += 1
        if i > N:
            break

    print(f"\nTotal de hombres: {total_hombres}")
    print(f"Total de mujeres: {total_mujeres}")

# Menú principal
while True:
    os.system("cls")
    print("===== MENÚ DE CENSO =====")
    print("1. Ejecutar con ciclo FOR")
    print("2. Ejecutar con ciclo WHILE")
    print("3. Ejecutar con ciclo REPEAT (simulado)")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        censo_for()
    elif opcion == "2":
        censo_while()
    elif opcion == "3":
        censo_repeat()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")

    os.system("pause")
