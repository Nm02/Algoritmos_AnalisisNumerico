def NewtonRaphson(f,fPrima,x,xant,E):
    if E<0:
        E=-E
    while fPrima(x)!=0:
        x=x-(f(x)/fPrima(x))
        if x==0:
            return x
        if -E<(((x-xant)/x)*100)<E:
            return x
        xant=x