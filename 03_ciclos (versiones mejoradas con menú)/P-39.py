import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def sumatoria_for():
    sumatoria = 0
    print("\nUsando FOR - Sumatoria del 1 al 10:")
    for i in range(1, 11):
        print(f"{i}", end=" + " if i < 10 else " = ")
        sumatoria += i
    print(sumatoria)
    return sumatoria

def sumatoria_while():
    sumatoria = 0
    i = 1
    print("\nUsando WHILE - Sumatoria del 1 al 10:")
    while i <= 10:
        print(f"{i}", end=" + " if i < 10 else " = ")
        sumatoria += i
        i += 1
    print(sumatoria)
    return sumatoria

def sumatoria_repeat():
    sumatoria = 0
    i = 1
    print("\nUsando REPEAT (simulado) - Sumatoria del 1 al 10:")
    while True:
        print(f"{i}", end=" + " if i < 10 else " = ")
        sumatoria += i
        i += 1
        if i > 10:
            break
    print(sumatoria)
    return sumatoria

def mostrar_menu():
    limpiar_pantalla()
    print("""
    MENÚ DE SUMATORIA (1-10)
    -------------------------
    1. Calcular con estructura FOR
    2. Calcular con estructura WHILE
    3. Calcular con estructura REPEAT
    4. Salir del programa
    """)

def main():
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ")
        
        if opcion == "1":
            resultado = sumatoria_for()
        elif opcion == "2":
            resultado = sumatoria_while()
        elif opcion == "3":
            resultado = sumatoria_repeat()
        elif opcion == "4":
            print("\n¡Programa finalizado!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue
        
        print(f"\nEl resultado de la sumatoria es: {resultado}")
        input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    main()