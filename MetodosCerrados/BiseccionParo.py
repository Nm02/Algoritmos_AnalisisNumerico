def Biseccion(f,a,b):
    if b>a:
        temp=a
        a=b
        b=temp
    elif a==b:
        if f(a)==0:
            return a
        else:
            print("No hay raices en el intervalo dado.")
            return None
    """f(x)==x**3+2*x**2+5"""
    if (f(a))*(f(b))<0:
        xr=(a+b)/2
        if (f(a))*(f(xr))<0:
            b=xr
        elif (f(xr))*(f(b))<0:
            a=xr
        else:
            return xr
        while True:
            xrant=xr
            xr=(a+b)/2
            if -0.001<(((xrant-xr)/xr)*100)<0.001:
                return xr
            if (f(a))*(f(xr))<0:
                b=xr
            elif (f(xr))*(f(b))<0:
                a=xr
            else:
                return xr
    else:
        print("No se puede concluir si hay o no raices por el metodo de la biseccion")
        return None

                

# a=int(input("ingrese el primer numero(a):"))
# b=int(input("ingrese el segundo numero(b):"))
