def Secante(f,x):
    xant=x-1
    while True:
        xtemp=xant
        xant=x
        
        if f(xtemp)-f(x)==0:
            return None
        
        x=x-((f(x)*(xtemp-x))/(f(xtemp)-f(x)))
        
        if x==0:
            return x
        if -0.1<(((x-xant)/x)*100)<0.1:
            return x