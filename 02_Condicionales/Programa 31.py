#Una familia de “n” integrantes, requiere un servicio de Taxi, para llegar a su hogar. Calcular el total a pagar por la familia, de acuerdo a las siguientes tarifas:
#Centro y colonias cercanas= $30, Colonias fuera de la ciudad= $45, Poblados del Plan Chontalpa más cercanos= $100, 4.Villahermosa= $150
import os, sys
os.system ("cls")
def calcular_total_taxi():
    # Mostrar las opciones de destino y sus tarifas
    print("Opciones de destino y tarifas:")
    print("1. Centro y colonias cercanas: $30 por persona")
    print("2. Colonias fuera de la ciudad: $45 por persona")
    print("3. Poblados del Plan Chontalpa más cercanos: $100 por persona")
    print("4. Villahermosa: $150 por persona")

    # Solicitar al usuario el número de integrantes y el destino
    integrantes = int(input("Ingresa el número de integrantes de la familia: "))
    destino = int(input("Elige el destino (1-4): "))

    # Definir la tarifa según el destino elegido
    if destino == 1:
        tarifa = 30
    elif destino == 2:
        tarifa = 45
    elif destino == 3:
        tarifa = 100
    elif destino == 4:
        tarifa = 150
    else:
        return "Destino no válido."

    # Calcular el total a pagar
    total_pagar = integrantes * tarifa

    return f"El total a pagar por {integrantes} integrantes es: ${total_pagar:.2f}"

# Llamar a la función y mostrar el resultado
print(calcular_total_taxi())
os.system ("pause")