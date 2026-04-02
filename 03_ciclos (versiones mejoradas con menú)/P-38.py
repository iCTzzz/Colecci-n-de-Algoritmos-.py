import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_impares_for():
    print("\nUsando FOR - Números impares del 1 al 50:")
    # Versión optimizada con paso 2 para mayor eficiencia
    for i in range(1, 51, 2):
        print(i, end=" ")
    print("\n\n(Cantidad de impares:", len(range(1, 51, 2)), ")")

def imprimir_impares_while():
    print("\nUsando WHILE - Números impares del 1 al 50:")
    i = 1
    count = 0
    while i <= 50:
        print(i, end=" ")
        i += 2
        count += 1
    print("\n\n(Cantidad de impares:", count, ")")

def imprimir_impares_repeat():
    print("\nUsando REPEAT (simulado) - Números impares del 1 al 50:")
    i = 1
    count = 0
    while True:  # Simulación de estructura REPEAT
        print(i, end=" ")
        i += 2
        count += 1
        if i > 50:
            break
    print("\n\n(Cantidad de impares:", count, ")")

def mostrar_menu():
    limpiar_pantalla()
    print("""
    MENÚ DE ESTRUCTURAS CÍCLICAS - NÚMEROS IMPARES (1-50)
    ----------------------------------------------------
    1. Imprimir usando estructura FOR
    2. Imprimir usando estructura WHILE
    3. Imprimir usando estructura REPEAT (simulada)
    4. Salir del programa
    """)

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            imprimir_impares_for()
        elif opcion == "2":
            imprimir_impares_while()
        elif opcion == "3":
            imprimir_impares_repeat()
        elif opcion == "4":
            print("\n¡Gracias por usar el programa! Hasta pronto.")
            break
        else:
            print("\nOpción no válida. Por favor ingrese 1, 2, 3 o 4.")
        
        input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    main()