def NewtonRaphson(f,fPrima,x):
    while fPrima(x)!=0:
        xant=x
        x=x-(f(x)/fPrima(x))
        if x==0:
            return x
        if -0.1<(((x-xant)/x)*100)<0.1:
            return x