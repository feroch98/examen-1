import numpy as np

# Matriz de coeficientes
A = np.array([[0.25, 0.15, 0], [0.45, 0.5, 0.75], [0.3, 0.35, 0.25]])

# Vector de términos independientes
b = np.array([1.5, 5, 3])

# Resolver el sistema de ecuaciones
x = np.linalg.solve(A, b)

# Mostrar la solución
print("Cantidad de fertilizante tipo A: {:.2f} toneladas".format(x[0]))
print("Cantidad de fertilizante tipo B: {:.2f} toneladas".format(x[1]))
print("Cantidad de fertilizante tipo C: {:.2f} toneladas".format(x[2]))
