import numpy as np
from tabulate import tabulate


def RK1(xi, yi, xf, h):
    n = (xf - xi) / h  # cantidad de intervalos
    x = np.linspace(xi, xf, int(n + 1))  # valores de x
    yf = []  # aproximacion de la integral de f'x
    fi = []  # derivada f'x
    k1v = []  # vector de k1
    yf.append(yi)
    er = ["--"]
    k1v.append("--")

    for i in range(int(n)):
        k1 = f1(x[i], yf[i])
        yf.append(yf[i] + k1 * h)
        er.append(abs((yf[i + 1] - yf[i]) * 100 / yf[i]))
        k1v.append(k1)

    return x, yf, k1v, er


# -------------------------------------------------------------------------------
# metodo de Runge - Kutta de segundo orden


def RK2(xi, yi, xf, h):
    n = (xf - xi) / h  # cantidad de intervalos
    x = np.linspace(xi, xf, int(n + 1))  # valores de x
    yf = []  # aproximacion de la integral de f'x
    fi = []  # derivada f'x
    k1v = []  # vector de k1
    k2v = []  # vector de k2
    yf.append(yi)
    er = ["--"]
    k1v.append("--")
    k2v.append("--")
    # a2 = 1/2                                            #Valor a2 equivalente al Metodo Heun
    # a2 = 1                                             #Valor a2 equivalente al Metodo del punto medio
    a2 = 2 / 3  # Valor a2 equivalente al Metodo de Ralston
    a1 = 1 - a2
    p1 = 1 / (2 * a2)
    q11 = 1 / (2 * a2)

    for i in range(int(n)):
        k1 = f1(x[i], yf[i])
        k2 = f1(x[i] + p1 * h, yf[i] + q11 * k1 * h)
        yf.append(yf[i] + (a1 * k1 + a2 * k2) * h)
        er.append(abs((yf[i + 1] - yf[i]) * 100 / yf[i]))
        k1v.append(k1)
        k2v.append(k2)

    return x, yf, k1v, k2v, er


# -------------------------------------------------------------------------------
# metodo de Runge - Kutta de cuarto orden


def RK4(xi, yi, xf, h):
    n = (xf - xi) / h  # cantidad de intervalos
    x = np.linspace(xi, xf, int(n + 1))  # valores de x
    yf = []  # aproximacion de la integral de f'x
    fi = []  # derivada f'x
    k1v = []  # vector de k1
    k2v = []  # vector de k2
    k3v = []  # vector de k3
    k4v = []  # vector de k4
    yf.append(yi)
    er = ["--"]
    k1v.append("--")
    k2v.append("--")
    k3v.append("--")
    k4v.append("--")

    for i in range(int(n)):
        k1 = f1(x[i], yf[i])
        k2 = f1(x[i] + (1 / 2) * h, yf[i] + (1 / 2) * k1 * h)
        k3 = f1(x[i] + (1 / 2) * h, yf[i] + (1 / 2) * k2 * h)
        k4 = f1(x[i] + h, yf[i] + k3 * h)
        yf.append(yf[i] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * h)
        er.append(abs((yf[i + 1] - yf[i]) * 100 / yf[i]))
        k1v.append(k1)
        k2v.append(k2)
        k3v.append(k3)
        k4v.append(k4)

    return x, yf, k1v, k2v, k3v, k4v, er


# Funcion ecuacion diferencial de primer orden f(x,y)

def f1(x, y):
    dvy1 = -2 * x + y * x
    return dvy1


def f11(x, y):
    dvy1 = -2 + (-2 * x + y * x) * x + y
    return dvy1


def f12(x, y):
    dvy1 = -2 + (-2 * x + y * x) * x + y
    return dvy1


# Solucion analitica
def y(x):
    fx = np.exp((2 / 3) * x ** 3 + 0.9996)
    return fx

if __name__=="__main__":

    # Valores iniciales
    xi = 0  # Valor inicial de 'x'
    yi = 1  # Valor inicial de 'y'

    # Limite superior de integracion
    xf = 5  # Valor final de 'x'

    # Tamaño de Paso o incremento
    h1 = 0.5  # Tamaño de paso

    # Runge - Kutta de 1er orden
    x1_RK1, yf1_RK1, k11_RK1, e1_RK1 = RK1(xi, yi, xf, h1)

    # Runge - Kutta de 2do orden
    x1_RK2, yf1_RK2, k11_RK2, k12_RK2, e1_RK2 = RK2(xi, yi, xf, h1)

    # Runge - Kutta de 4to orden
    x1, yf1, k11, k12, k13, k14, e1 = RK4(xi, yi, xf, h1)

    # Runge-Kutta de 1er orden

    print("RUNGE - KUTTA 1er orden")
    print(" ")

    # Tabla 1
    n1 = len(x1)
    tabla1 = []  # tabla de datos
    # Llenar la tabla de datos
    for i in range(n1):
        tabla1.append([x1_RK1[i], yf1_RK1[i], k11_RK1[i], e1_RK1[i]])

    print("tabla de datos 1")
    print(" ")
    print(tabulate(tabla1, headers=['x', 'y', 'k1', 'er(%)']))
    print(" ")
    print(" ")

    # ------------------------------------------------------------------------------
    # Runge-Kutta de 2do orden
    print(" ")
    print(" ")
    print("RUNGE - KUTTA 2do orden")
    print(" ")

    # Tabla 1
    n1 = len(x1)
    tabla1 = []  # tabla de datos
    # Llenar la tabla de datos
    for i in range(n1):
        tabla1.append([x1_RK2[i], yf1_RK2[i], k11_RK2[i], k12_RK2[i], e1_RK2[i]])

    print("tabla de datos 1")
    print(" ")
    print(tabulate(tabla1, headers=['x', 'y', 'k1', 'k2', 'er(%)']))
    print(" ")
    print(" ")

    # ------------------------------------------------------------------------------
    # Runge-Kutta de 4to orden
    print(" ")
    print(" ")
    print("RUNGE - KUTTA 4to orden")
    print(" ")

    # Tabla 1
    n1 = len(x1)
    tabla1 = []  # tabla de datos
    # Llenar la tabla de datos
    for i in range(n1):
        tabla1.append([x1[i], yf1[i], k11[i], k12[i], k13[i], k14[i], e1[i]])

    print("tabla de datos 1")
    print(" ")
    print(tabulate(tabla1, headers=['x', 'y', 'k1', 'k2', 'k3', 'k4', 'er(%)']))
    print(" ")
    print(" ")
