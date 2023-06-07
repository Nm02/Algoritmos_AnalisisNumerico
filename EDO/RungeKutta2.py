def rk1(f, x0, y0, h, n):
    """
    Esta función implementa el método de Runge-Kutta de primer orden para resolver una ecuación diferencial ordinaria.

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


def rk2(f, x0, y0, h, n):
    """
    Esta función implementa el método de Runge-Kutta de segundo orden para resolver una ecuación diferencial ordinaria.

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
        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)
        y += 0.5 * (k1 + k2)
        x += h
        result.append((x, y))
    return result


def rk3(f, x0, y0, h, n):
    """
    Esta función implementa el método de Runge-Kutta de tercer orden para resolver una ecuación diferencial ordinaria.

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
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + h, y - k1 + 2 * k2)
        y += 1/6 * (k1 + 4*k2 + k3)
        x += h
        result.append((x, y))
    return result

def rk4(f, x0, y0, h, n):
    """
    Esta función implementa el método de Runge-Kutta de cuarto orden para resolver una ecuación diferencial ordinaria.

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
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        y += 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        x += h
        result.append((x, y))
    return result

import numpy as np

def rk4_system(f, x0, y0, h, n):
    """
    Esta función implementa el método de Runge-Kutta de cuarto orden para resolver un sistema de ecuaciones diferenciales ordinarias.

    Parámetros:
    f: Función de las ecuaciones diferenciales ordinarias, que toma como entrada un valor de x y un vector de valores de y y devuelve un vector de las derivadas de y.
    x0: Valor inicial de x.
    y0: Vector de valores iniciales de y.
    h: Tamaño del paso.
    n: Número de pasos.

    Retorno:
    Una lista de tuplas (x_i, y_i) que representan los valores de x e y en cada paso.
    """
    x = x0
    y = y0
    result = [(x, y)]
    for i in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        y += 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        x += h
        result.append((x, y))
    return result

if __name__=="__main__":
    pass