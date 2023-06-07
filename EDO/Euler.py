def euler(f, x0, y0, h, n):
    resultado = [(x0,y0)]
    for i in range(n):
        xi, yi = resultado[-1]
        fi = f(xi, yi)
        y_next = yi + h * fi
        x_next = xi + h
        resultado.append((x_next, y_next))
    return resultado


def f(x, y):
    return -2*(x**3)+12*(x**2)-20*x+8.5 #colocar funcion

if __name__=="__main__":
    resultado = euler(f, 0, 0, 0.5, 10)
    for x, y in resultado:
        print(f"x={x:.1f}, y={y:.5f}")