import numpy as np
def Euler(f, x0, y0, h, n):
    """
    Esta función implementa el método de Euler para resolver una ecuación diferencial ordinaria.

    Parámetros:
    f: Función de la ecuación diferencial ordinaria f(x, y).
    x0: Valor inicial de x.
    y0: Valor inicial de y.
    h: Tamaño del paso.
    n: Número de pasos.

    Retorno:
    Una lista de tuplas (x_i, y_i) que representan los valores de x e y en cada paso.
    """
    x = x0
    y = y0
    result = [(x, y)]
    for i in range(n):
        y += h * f(x, y)
        x += h
        result.append((x, y))
    return result

def euler_system(f, x0, y0, h, n):
    """
    Esta función implementa el método de Euler para resolver un sistema de ecuaciones diferenciales.

    Parámetros:
    f: Función del sistema de ecuaciones diferenciales f(x, y).
    x0: Valor inicial de x.
    y0: Lista o arreglo NumPy de valores iniciales de y.
    h: Tamaño del paso.
    n: Número de pasos.

    Retorno:
    Una lista de tuplas (x_i, y_i) que representan los valores de x e y en cada paso.
    """
    x = x0
    y = np.array(y0)
    result = [(x, y)]
    for i in range(n):
        y += h * f(x, y)
        x += h
        result.append((x, y))
    return result

def f(x,y):
    return