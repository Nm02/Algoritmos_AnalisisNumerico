def RegulaFalsi(f,a,b):
    if b>a:
        temp=a
        a=b
        b=temp
    elif a==b:
        if f(a)==0:
            print(f"Hay una raiz en {a}.")
        else:
            print("No hay raices en el intervalo dado.")
    """f(x)==x**3+2*x**2+5"""
    if ((f(a))*(f(b))<0):
        mr=b-((f(b))*(a-b)/((f(a))-(f(b))))
        if ((f(a))*(f(mr))<0):
            b=mr
        elif (f(mr))*(f(b))<0:
            a=mr
        else:
            return mr
        while True:
            mrant=mr
            mr=b-((f(b))*(a-b)/((f(a))-(f(b))))
            if -0.001<(((mr-mrant)/mr)*100)<0.001:
                return mr
            if ((f(a))*(f(mr))<0):
                b=mr
            elif (f(mr))*(f(b))<0:
                a=mr
            else:
                return mr
    else:
        print("No se puede derterminar si hay raices en el intervalo con el metodo de regula falsi")
        return None

a=int(input("ingrese el primer numero(a):"))
b=int(input("ingrese el segundo numero(b):"))
RegulaFalsi(lambda x:x**2-2,a,b)