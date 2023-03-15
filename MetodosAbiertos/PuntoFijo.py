def PuntoFijo(g,gPrima,x,n=100000):
    if(g(x)==0):
        return x
    elif gPrima(x)<1:
        for i in range(n):
            print(x)
            x=g(x)
            if x==0:
                return x
        return x