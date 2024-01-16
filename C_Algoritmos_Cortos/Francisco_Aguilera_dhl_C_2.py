# PRUEBA C.2 - ALGORITMOS CORTOS
# Francisco Rolando Aguilera Portillo

# 2.	Escriba un script que cuente con una función que solicite al usuario ingresar una cadena de 
# caracteres se deberá imprimir en pantalla:
# a.	Cantidad de caracteres ingresados
# b.	La misma cadena de caracteres pero traspuesta -> Ej.: “Hola” -> ”aloH”

def invertir_cadena():
    cadena = input("Por favor, ingrese una cadena de caracteres: ")

    # a. Imprime la cantidad de caracteres ingresados utilizando len()
    caracteres = len(cadena)
    print(f"\nCantidad de caracteres ingresados: {caracteres}")

    # b. Traspone la cadena ingresada usando el comodín [::-1]
    resultado = cadena[::-1]
    print(f"Cadena de caracteres traspuesta: {resultado}")

# El main del programa llama a la función requerida
invertir_cadena()
