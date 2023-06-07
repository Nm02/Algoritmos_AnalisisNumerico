import numpy as np

# Matriz de coeficientes
A = np.array([[0.2, 1.3, -4, 1.25, 5],
              [0.03, 0.2, -0.6, 0.19, 0.75],
              [0.19, 1.24, -3.82, 0.19, 4.77],
              [0.29, 1.88, -5.78, 1.81, 7.23],
              [-0.06, -0.39, 1.2, -0.38, -1.5]])

# Vector de resultados
b = np.array([8, -2.4, 1.2, 7.63, 11.56])

# Resolver el sistema de ecuaciones utilizando mínimos cuadrados
x, residuals, rank, singular_values = np.linalg.lstsq(A, b, rcond=None)

# Mostrar la solución
print("Solución:")
print(x)


