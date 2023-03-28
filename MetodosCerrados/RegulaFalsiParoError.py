def RegulaFalsi(f,a,b,E):
    if E<0:
        E=-E
    if b>a:
        temp=a
        a=b
        b=temp
    elif a==b:
        if f(a)==0:
            print(f"Hay una raiz en {a}.")
        else:
            print("No hay raices en el intervalo dado.")
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
            if -E<(((mr-mrant)/mr)*100)<E:
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

# a=int(input("ingrese el primer numero(a):"))
# b=int(input("ingrese el segundo numero(b):"))
