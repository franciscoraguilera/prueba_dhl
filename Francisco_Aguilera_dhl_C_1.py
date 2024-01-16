# PRUEBA C.1 - ALGORITMOS CORTOS
# Francisco Rolando Aguilera Portillo

# 1. Cree una lista de números del 1 al 20 e imprima en pantalla todos los números que sean pares, los números 
# que sean impares deben ser almacenados en una variable y sumados para mostrar el resultado final.

# Creamos una lista del 1 al 20 con list()
numeros = list(range(1, 21))

# Se inicializan las variables y estructuras necesarias para almacenar los datos
suma_impares = 0
pares = []

for numero in numeros:
    # Verifica si el número es par mediante módulo
    if numero % 2 == 0:
        pares.append(numero)
    else:
        # Si el número es impar, se hace un acumulador
        suma_impares += numero

# Muestra los resultados
        
print("\n Números pares:")
print(*pares, sep = ", ")

print(f"\n Suma de números impares: {suma_impares}")