import math
def PuntoFijo(g,gPrima,x,E):
    if E<0:
        E=-E
    if(g(x)==0):
        return x
    elif gPrima(x)<1:
        while True:
            x=round(x,4)
            xant=x
            x=g(x)
            if x==0:
                return x
            elif -E<float(((x-xant)/x)*100)<E:
                return x

