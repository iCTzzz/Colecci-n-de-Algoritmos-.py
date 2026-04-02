import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def promedio_for():
    limpiar_pantalla()
    print("\nCÁLCULO DE PROMEDIO (usando FOR)")
    try:
        n = int(input("Ingrese el número de materias cursadas: "))
        if n <= 0:
            print("El número de materias debe ser mayor a cero")
            return None
        
        suma = 0.0
        for i in range(1, n+1):
            calificacion = float(input(f"Ingrese la calificación {i}/{n}: "))
            if calificacion < 0 or calificacion > 10:
                print("Las calificaciones deben estar entre 0 y 10")
                return None
            suma += calificacion
        
        return suma / n
        
    except ValueError:
        print("Error: Debe ingresar valores numéricos")
        return None

def promedio_while():
    limpiar_pantalla()
    print("\nCÁLCULO DE PROMEDIO (usando WHILE)")
    try:
        n = int(input("Ingrese el número de materias cursadas: "))
        if n <= 0:
            print("El número de materias debe ser mayor a cero")
            return None
        
        suma = 0.0
        i = 1
        while i <= n:
            calificacion = float(input(f"Ingrese la calificación {i}/{n}: "))
            if calificacion < 0 or calificacion > 10:
                print("Las calificaciones deben estar entre 0 y 10")
                return None
            suma += calificacion
            i += 1
        
        return suma / n
        
    except ValueError:
        print("Error: Debe ingresar valores numéricos")
        return None

def promedio_repeat():
    limpiar_pantalla()
    print("\nCÁLCULO DE PROMEDIO (usando REPEAT simulado)")
    try:
        n = int(input("Ingrese el número de materias cursadas: "))
        if n <= 0:
            print("El número de materias debe ser mayor a cero")
            return None
        
        suma = 0.0
        i = 1
        while True:  # Simulación de estructura REPEAT
            calificacion = float(input(f"Ingrese la calificación {i}/{n}: "))
            if calificacion < 0 or calificacion > 10:
                print("Las calificaciones deben estar entre 0 y 10")
                return None
            suma += calificacion
            i += 1
            if i > n:
                break
        
        return suma / n
        
    except ValueError:
        print("Error: Debe ingresar valores numéricos")
        return None

def mostrar_menu():
    limpiar_pantalla()
    print("""
    SISTEMA DE CÁLCULO DE PROMEDIOS
    -------------------------------
    1. Calcular promedio usando FOR
    2. Calcular promedio usando WHILE
    3. Calcular promedio usando REPEAT
    4. Salir del programa
    """)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            resultado = promedio_for()
        elif opcion == "2":
            resultado = promedio_while()
        elif opcion == "3":
            resultado = promedio_repeat()
        elif opcion == "4":
            print("\n¡Gracias por usar el sistema de promedios!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue
        
        if resultado is not None:
            print(f"\nEl promedio general es: {resultado:.2f}")
        
        input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    main()