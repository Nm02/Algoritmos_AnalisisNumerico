def Secante(f,x,n=100000):
    xant=x-1
    for i in range(n):
        xtemp=xant
        xant=x
        x=x-((f(x)*(xtemp-x))/(f(xtemp)-f(x)))
        
        if x==0:
            return x
        if -0.1<(((x-xant)/x)*100)<0.1:
            return x