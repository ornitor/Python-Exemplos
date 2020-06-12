import math

def soma(a,b):
    return (a[0]+b[0],a[1]+b[1])

def sub(a,b):
    return (a[0]-b[0],a[1]-b[1])

def modulo(a):
    return math.sqrt(a[0]*a[0] + a[1]*a[1])

def distancia(a,b):
    return modulo(sub(a,b))

def unitario(a):
    return mux(1/modulo(a),a)

def mux(k,a):
    return (k*a[0],k*a[1])

def pescalar(a,b):
    return a[0]*b[0] + a[1]*b[1]

def campo(e,a,b):
    c = sub(a,b)
    d = modulo(c) + 20
    cc = mux( 1e5*e/(d*d) ,unitario(c))
    dd = soma(b,c)
    return cc

def integral(x,y,dt):
    return soma(y,mux(dt,x))

zx = (0,0)
ww = (8,6)

print (zx+ ww)
print (modulo(ww))
print (unitario(ww))
print (distancia(ww,zx))
print (campo(25,ww,zx))
