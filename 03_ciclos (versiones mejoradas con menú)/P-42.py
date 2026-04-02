import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def sumatoria_pares_for():
    limpiar_pantalla()
    print("\nSUMATORIA DE PARES (usando FOR)")
    try:
        N = int(input("Ingrese el valor límite N: "))
        if N < 2:
            print("El número debe ser mayor o igual a 2")
            return None
        
        suma = 0
        print("\nProceso de suma:")
        for i in range(2, N+1, 2):
            print(f"Sumando {i}", end=" → " if i < N-1 else " = ")
            suma += i
        return suma
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
        return None

def sumatoria_pares_while():
    limpiar_pantalla()
    print("\nSUMATORIA DE PARES (usando WHILE)")
    try:
        N = int(input("Ingrese el valor límite N: "))
        if N < 2:
            print("El número debe ser mayor o igual a 2")
            return None
        
        suma = 0
        i = 2
        print("\nProceso de suma:")
        while i <= N:
            print(f"Sumando {i}", end=" → " if i < N-1 else " = ")
            suma += i
            i += 2
        return suma
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
        return None

def sumatoria_pares_repeat():
    limpiar_pantalla()
    print("\nSUMATORIA DE PARES (usando REPEAT simulado)")
    try:
        N = int(input("Ingrese el valor límite N: "))
        if N < 2:
            print("El número debe ser mayor o igual a 2")
            return None
        
        suma = 0
        i = 2
        print("\nProceso de suma:")
        while True:  # Simulación de estructura REPEAT
            print(f"Sumando {i}", end=" → " if i < N-1 else " = ")
            suma += i
            i += 2
            if i > N:
                break
        return suma
        
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
        return None

def mostrar_menu():
    limpiar_pantalla()
    print("""
    SUMATORIA DE NÚMEROS PARES (2 hasta N)
    --------------------------------------
    1. Calcular usando estructura FOR
    2. Calcular usando estructura WHILE
    3. Calcular usando estructura REPEAT
    4. Salir del programa
    """)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            resultado = sumatoria_pares_for()
        elif opcion == "2":
            resultado = sumatoria_pares_while()
        elif opcion == "3":
            resultado = sumatoria_pares_repeat()
        elif opcion == "4":
            print("\n¡Gracias por usar el programa!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue
        
        if resultado is not None:
            print(f"\n\nEl resultado de la sumatoria es: {resultado}")
        
        input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    main()