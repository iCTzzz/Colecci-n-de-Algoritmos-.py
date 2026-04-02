import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def tabla_for(numero):
    print(f"\nTabla del {numero} usando FOR:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

def tabla_while(numero):
    print(f"\nTabla del {numero} usando WHILE:")
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1

def tabla_repeat(numero):
    print(f"\nTabla del {numero} usando REPEAT (simulado):")
    i = 1
    while True:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
        if i > 10:
            break

def mostrar_menu_estructuras():
    print("""
    ELIJA LA ESTRUCTURA CÍCLICA:
    1. Usar estructura FOR
    2. Usar estructura WHILE
    3. Usar estructura REPEAT
    4. Volver al menú principal
    """)

def mostrar_menu_principal():
    limpiar_pantalla()
    print("""
    TABLAS DE MULTIPLICAR
    ---------------------
    1. Generar tabla de multiplicar
    2. Salir del programa
    """)

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Seleccione una opción (1-2): ")
        
        if opcion_principal == "1":
            try:
                numero = int(input("\nIngrese el número para la tabla de multiplicar (1-10): "))
                if numero < 1 or numero > 10:
                    print("El número debe estar entre 1 y 10")
                    input("Presione Enter para continuar...")
                    continue
                    
                while True:
                    mostrar_menu_estructuras()
                    opcion_estructura = input("Seleccione estructura cíclica (1-4): ")
                    
                    if opcion_estructura == "1":
                        tabla_for(numero)
                    elif opcion_estructura == "2":
                        tabla_while(numero)
                    elif opcion_estructura == "3":
                        tabla_repeat(numero)
                    elif opcion_estructura == "4":
                        break
                    else:
                        print("Opción no válida")
                    
                    input("\nPresione Enter para continuar...")
                    
            except ValueError:
                print("Debe ingresar un número válido")
                input("Presione Enter para continuar...")
                
        elif opcion_principal == "2":
            print("\n¡Gracias por usar el programa!")
            break
            
        else:
            print("Opción no válida")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()