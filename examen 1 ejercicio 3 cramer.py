import numpy as np

# Definimos la matriz A y el vector b
A = np.array([[0.25, 0.15, 0], [0.45, 0.5, 0.75], [0.3, 0.35, 0.25]])
b = np.array([1.5, 5, 3])

# Calculamos el determinante de A y los determinantes de A1, A2 y A3
detA = np.linalg.det(A)

A1 = A.copy()
A1[:, 0] = b
detA1 = np.linalg.det(A1)

A2 = A.copy()
A2[:, 1] = b
detA2 = np.linalg.det(A2)

A3 = A.copy()
A3[:, 2] = b
detA3 = np.linalg.det(A3)

# Calculamos las soluciones del sistema
x = detA1 / detA
y = detA2 / detA
z = detA3 / detA

# Imprimimos las soluciones
print("Cantidad de toneladas de fertilizante tipo A a producir:", x)
print("Cantidad de toneladas de fertilizante tipo B a producir:", y)
print("Cantidad de toneladas de fertilizante tipo C a producir:", z)
