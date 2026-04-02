import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_for():
    print("\nUsando FOR:")
    for i in range(1, 11):
        print(i, end=" ")
    print()

def imprimir_while():
    print("\nUsando WHILE:")
    i = 1
    while i <= 10:
        print(i, end=" ")
        i += 1
    print()

def imprimir_repeat():
    print("\nUsando REPEAT (simulado con while True):")
    i = 1
    while True:  # Esto simula el REPEAT
        print(i, end=" ")
        i += 1
        if i > 10:
            break
    print()

def mostrar_menu():
    limpiar_pantalla()
    print("""
    MENÚ DE ESTRUCTURAS CÍCLICAS
    ----------------------------
    1. Imprimir con FOR
    2. Imprimir con WHILE
    3. Imprimir con REPEAT (simulado)
    4. Salir
    """)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            imprimir_for()
        elif opcion == "2":
            imprimir_while()
        elif opcion == "3":
            imprimir_repeat()
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()