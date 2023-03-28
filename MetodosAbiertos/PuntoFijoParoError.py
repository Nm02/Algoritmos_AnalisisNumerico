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
            print(x)
            print(type(x))
            # if x==0:
            #     return x
            # elif -E<float(((x-xant)/x)*100)<E:
            #     return x


# def g(x):
#     return math.sqrt(10*math.cos(x))

"""
g'(x)=-((5*math.sin(x)/((10*math.cos(x))**1/2)))
"""
# def gPrima(x):
#     return -((5*math.sin(x)/((10*math.cos(x))**1/2)))

g=lambda x:math.sqrt(10*math.cos(x))
gPrima=lambda x:-((5*math.sin(x)/((10*math.cos(x))**1/2)))
x0=1.5
xant=1.2
E=10*math.exp(-7)

print(g(2.5819))