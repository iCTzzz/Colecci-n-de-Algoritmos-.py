import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpiar_pantalla()
    print("""
    SUMATORIA DE NÚMEROS IMPARES (1 hasta N)
    ----------------------------------------
    1. Calcular usando estructura FOR
    2. Calcular usando estructura WHILE
    3. Calcular usando estructura REPEAT
    4. Salir del programa
    """)

def sumatoria_for():
    try:
        N = int(input("\nIngrese el valor de N: "))
        if N < 1:
            print("Error: N debe ser mayor o igual a 1")
            return None
        
        suma = 0
        print("\nProceso de cálculo:")
        for i in range(1, N + 1, 2):
            print(f"Sumando {i}", end=" → " if i < N - (0 if N % 2 else 1) else " = ")
            suma += i
        return suma
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
        return None

def sumatoria_while():
    try:
        N = int(input("\nIngrese el valor de N: "))
        if N < 1:
            print("Error: N debe ser mayor o igual a 1")
            return None
        
        suma = 0
        i = 1
        print("\nProceso de cálculo:")
        while i <= N:
            print(f"Sumando {i}", end=" → " if i < N - (0 if N % 2 else 1) else " = ")
            suma += i
            i += 2
        return suma
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
        return None

def sumatoria_repeat():
    try:
        N = int(input("\nIngrese el valor de N: "))
        if N < 1:
            print("Error: N debe ser mayor o igual a 1")
            return None
        
        suma = 0
        i = 1
        print("\nProceso de cálculo:")
        while True:  # Simulación de REPEAT
            print(f"Sumando {i}", end=" → " if i < N - (0 if N % 2 else 1) else " = ")
            suma += i
            i += 2
            if i > N:
                break
        return suma
    except ValueError:
        print("Error: Debe ingresar un número entero válido")
        return None

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
            print("\n¡Gracias por usar el programa!")
            break
        else:
            print("\nOpción no válida. Por favor ingrese 1, 2, 3 ó 4.")
            input("Presione Enter para continuar...")
            continue
        
        if resultado is not None:
            print(f"\n\nLa sumatoria de números impares es: {resultado}")
        
        input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    main()