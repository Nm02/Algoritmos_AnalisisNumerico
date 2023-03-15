def NewtonRaphson(f,fPrima,x,n=100000):
    for i in range(n):
        if fPrima(x)!=0:
            xant=x
            x=x-(f(x)/fPrima(x))
            if x==0:
                return x
            if -0.1<(((x-xant)/x)*100)<0.1:
                return x