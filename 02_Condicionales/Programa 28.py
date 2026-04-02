#Calcular el total a pagar por una familia de “N” integrantes, que desea hacer un viaje a cualquiera de los siguientes destinos:
#Cárdenas - Villahermosa: Costo del boleto = $50, Cárdenas - Coatzacoalcos: Costo del boleto = $120, Cárdenas - Veracruz: Costo del boleto = $300 , Cárdenas - CDMX: Costo del boleto = $800
import os, sys
os.system ("cls")
def calcular_total_viaje():
    # Mostrar los destinos y sus costos
    print("Destinos disponibles:")
    print("1. Cárdenas - Villahermosa: $50 por boleto")
    print("2. Cárdenas - Coatzacoalcos: $120 por boleto")
    print("3. Cárdenas - Veracruz: $300 por boleto")
    print("4. Cárdenas - CDMX: $800 por boleto")

    # Solicitar al usuario el número de integrantes y el destino
    integrantes = int(input("Ingresa el número de integrantes de la familia: "))
    destino = int(input("Elige el destino (1-4): "))

    # Definir el costo del boleto según el destino elegido
    if destino == 1:
        costo_boleto = 50
    elif destino == 2:
        costo_boleto = 120
    elif destino == 3:
        costo_boleto = 300
    elif destino == 4:
        costo_boleto = 800
    else:
        return "Destino no válido."

    # Calcular el total a pagar
    total_pagar = integrantes * costo_boleto

    return f"El total a pagar por {integrantes} integrantes es: ${total_pagar:.2f}"

# Llamar a la función y mostrar el resultado
print(calcular_total_viaje())
os.system ("pause")