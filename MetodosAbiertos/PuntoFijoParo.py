def PuntoFijo(g,gPrima,x):
    if(g(x)==0):
        return x
    elif gPrima(x)<1:
        while True:
            xant=x
            x=g(x)
            if x==0:
                return x
            elif -0.1<(((x-xant)/x)*100)<0.1:
                return x