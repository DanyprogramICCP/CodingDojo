numeros_str = input("Ingrese los números separados por comas: ")

# Convertimos los números ingresados en una lista de enteros
numeros = [int(num) for num in numeros_str.split(',')]

# Calculamos el promedio de los números
promedio = sum(numeros) / len(numeros)

# Imprimimos el resultado
print("El promedio es:", promedio)