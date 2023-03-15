def RegulaFalsi(f,a,b,n=10000):
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
        for i in range(n):
            mr=b-((f(b))*(a-b)/((f(a))-(f(b))))
            if ((f(a))*(f(mr))<0):
                b=mr
            elif (f(mr))*(f(b))<0:
                a=mr
            else:
                return mr
        return mr
    else:
        print("No se puede derterminar si hay raices en el intervalo con el metodo de regula falsi")
        return None

                
# a=int(input("ingrese el primer numero(a):"))
# b=int(input("ingrese el segundo numero(b):"))
