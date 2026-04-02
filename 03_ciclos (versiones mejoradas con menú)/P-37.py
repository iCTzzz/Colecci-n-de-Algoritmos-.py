import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_pares_for():
    print("\nUsando FOR - Números pares del 20 al 30:")
    for i in range(20, 31):
        if i % 2 == 0:
            print(i, end=" ")
    print()

def imprimir_pares_while():
    print("\nUsando WHILE - Números pares del 20 al 30:")
    i = 20
    while i <= 30:
        if i % 2 == 0:
            print(i, end=" ")
        i += 1
    print()

def imprimir_pares_repeat():
    print("\nUsando REPEAT (simulado) - Números pares del 20 al 30:")
    i = 20
    while True:  # Esto simula el REPEAT
        if i % 2 == 0:
            print(i, end=" ")
        i += 1
        if i > 30:
            break
    print()

def mostrar_menu():
    limpiar_pantalla()
    print("""
    MENÚ DE ESTRUCTURAS CÍCLICAS
    ----------------------------
    1. Imprimir pares con FOR
    2. Imprimir pares con WHILE
    3. Imprimir pares con REPEAT (simulado)
    4. Salir
    """)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            imprimir_pares_for()
        elif opcion == "2":
            imprimir_pares_while()
        elif opcion == "3":
            imprimir_pares_repeat()
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()