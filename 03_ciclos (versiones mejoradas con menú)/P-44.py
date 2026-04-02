import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    limpiar_pantalla()
    print("""
    PROMEDIO DE ESTATURA Y PESO DE ALUMNOS
    --------------------------------------
    1. Calcular usando FOR
    2. Calcular usando WHILE
    3. Calcular usando REPEAT
    4. Salir del programa
    """)

def calcular_con_for():
    limpiar_pantalla()
    print("\nCÁLCULO CON ESTRUCTURA FOR")
    try:
        N = int(input("Ingrese el número de alumnos: "))
        if N <= 0:
            print("Error: Debe ingresar un número mayor a cero")
            return None, None
        
        suma_estatura = 0.0
        suma_peso = 0.0
        
        for i in range(1, N+1):
            print(f"\nAlumno {i}/{N}:")
            try:
                estatura = float(input("Estatura (metros): "))
                peso = float(input("Peso (kg): "))
                
                if estatura <= 0 or peso <= 0:
                    print("Error: Los valores deben ser positivos")
                    return None, None
                    
                suma_estatura += estatura
                suma_peso += peso
            except ValueError:
                print("Error: Ingrese valores numéricos válidos")
                return None, None
                
        return suma_estatura/N, suma_peso/N
        
    except ValueError:
        print("Error: Ingrese un número entero válido")
        return None, None

def calcular_con_while():
    limpiar_pantalla()
    print("\nCÁLCULO CON ESTRUCTURA WHILE")
    try:
        N = int(input("Ingrese el número de alumnos: "))
        if N <= 0:
            print("Error: Debe ingresar un número mayor a cero")
            return None, None
        
        suma_estatura = 0.0
        suma_peso = 0.0
        i = 1
        
        while i <= N:
            print(f"\nAlumno {i}/{N}:")
            try:
                estatura = float(input("Estatura (metros): "))
                peso = float(input("Peso (kg): "))
                
                if estatura <= 0 or peso <= 0:
                    print("Error: Los valores deben ser positivos")
                    return None, None
                    
                suma_estatura += estatura
                suma_peso += peso
                i += 1
            except ValueError:
                print("Error: Ingrese valores numéricos válidos")
                return None, None
                
        return suma_estatura/N, suma_peso/N
        
    except ValueError:
        print("Error: Ingrese un número entero válido")
        return None, None

def calcular_con_repeat():
    limpiar_pantalla()
    print("\nCÁLCULO CON ESTRUCTURA REPEAT (SIMULADA)")
    try:
        N = int(input("Ingrese el número de alumnos: "))
        if N <= 0:
            print("Error: Debe ingresar un número mayor a cero")
            return None, None
        
        suma_estatura = 0.0
        suma_peso = 0.0
        i = 1
        
        while True:  # Simulación de REPEAT
            print(f"\nAlumno {i}/{N}:")
            try:
                estatura = float(input("Estatura (metros): "))
                peso = float(input("Peso (kg): "))
                
                if estatura <= 0 or peso <= 0:
                    print("Error: Los valores deben ser positivos")
                    return None, None
                    
                suma_estatura += estatura
                suma_peso += peso
                i += 1
                if i > N:
                    break
            except ValueError:
                print("Error: Ingrese valores numéricos válidos")
                return None, None
                
        return suma_estatura/N, suma_peso/N
        
    except ValueError:
        print("Error: Ingrese un número entero válido")
        return None, None

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            prom_estatura, prom_peso = calcular_con_for()
        elif opcion == "2":
            prom_estatura, prom_peso = calcular_con_while()
        elif opcion == "3":
            prom_estatura, prom_peso = calcular_con_repeat()
        elif opcion == "4":
            print("\n¡Gracias por usar el programa!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")
            continue
        
        if prom_estatura is not None and prom_peso is not None:
            print("\n" + "="*40)
            print(f"RESULTADOS FINALES:")
            print(f"Promedio de estatura: {prom_estatura:.2f} metros")
            print(f"Promedio de peso: {prom_peso:.2f} kg")
            print("="*40)
        
        input("\nPresione Enter para volver al menú...")

if __name__ == "__main__":
    main()