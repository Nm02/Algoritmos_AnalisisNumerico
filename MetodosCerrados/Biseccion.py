import Funciones 

def Biseccion(f,a,b,n=1000):
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
        for i in range(n):
            xr=(a+b)/2
            if (f(a))*(f(xr))<0:
                b=xr
            elif (f(xr))*(f(b))<0:
                a=xr
            else:
                return xr
        return xr
    else:
        print("No se puede concluir si hay o no raices por el metodo de la biseccion")
        return None

                

# a=int(input("ingrese el primer numero(a):"))
# b=int(input("ingrese el segundo numero(b):"))
# n=int(input("Ingrese cantidad de iteraciones:"))
