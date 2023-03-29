def Biseccion(f,a,b,E):
    if E<0:
        E=-E
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
            if -E<(((xrant-xr)/xr)*100)<E:
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
