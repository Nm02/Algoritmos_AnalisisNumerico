def Secante(f,x,xant,E):
    if E<0:
        E=-E
    while True:
        xtemp=xant
        xant=x
        
        if f(xtemp)-f(x)==0:
            return None
        
        x=x-((f(x)*(xtemp-x))/(f(xtemp)-f(x)))
        
        if x==0:
            return x
        if -E<(((x-xant)/x)*100)<E:
            return x