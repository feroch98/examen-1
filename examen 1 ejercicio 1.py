def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sumar_diagonal_superior(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i < j:
                suma += matriz[i][j]
    return suma

# Pedimos al usuario que ingrese la dimensión de la matriz
m = int(input("Ingrese la dimensión de la matriz (mayor o igual a 3): "))

while m < 3:
    m = int(input("Ingrese un valor mayor o igual a 3: "))

# Construimos la matriz de m x m con los primeros m x m números primos
matriz = []
num_primos = 0
num = 2

while num_primos < m**2:
    if es_primo(num):
        num_primos += 1
        if num_primos % m == 1:
            matriz.append([num])
        else:
            matriz[-1].append(num)
    num += 1

# Mostramos la matriz 
for fila in matriz:
    fila_str = " ".join(str(num) for num in fila)
    print(fila_str)

# Sumamos los elementos de la diagonal superior y mostramos el resultado
suma_diagonal = sumar_diagonal_superior(matriz)
print("La suma de los elementos de la diagonal superior es:", suma_diagonal)
