import math
def suma(x, y):
    return x+y

def resta(x, y):
    return x - y

def raiz(x):
    return math.sqrt(x)

def potn(x):
    return x**2

def divis(x, y):
    return x/y
    
b= suma(0, 2)
a = 3
b = -2
c = -3
""""
potn(b) #El cuadrado de b
4*a*c   #El producto de 4, a y c
resta(pont(b), 4*a*c) #Resta de b^2 con 4ac
raiz(resta(pont(b), 4*a*c)) #La raiz cuadrada de la resta de b^2 con
x1 = divis(suma(-b, raiz(resta(pont(b), 4*a*c))), 2*a)
x2 = divis(resta(-b, raiz(resta(pont(b), 4*a*c))), 2*a)
"""
x1 = divis(suma(-b, raiz(resta(potn(b), 4*a*c))), 2*a)
x2 = divis(resta(-b, raiz(resta(potn(b), 4*a*c))), 2*a)
print(f"Las soluciones del trinomio\n{a}x^2+{b}x+{c}\n son {x1} y {x2}")








