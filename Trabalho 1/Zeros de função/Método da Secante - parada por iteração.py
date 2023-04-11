import math

def secante(f,x_0, x_1, lista):
    n = max(lista)
    raiz = x_0
    for i in range(n):
        if f(x_0) - f(x_1) != 0: # se a derivada for zero sai    
            raiz= (x_0*f(x_1) - x_1*f(x_0)) / (f(x_1) - f(x_0))
        if (i + 1) in lista:
            print(f"{raiz},")
        
        x_0 = x_1
        x_1 = raiz
    return 

# teste :

func = lambda x: math.pi*x-math.exp(x)
x0 = 1.29405
x1 = 2.17217
iterations = [1, 3, 5]
secante(func, x0, x1, iterations)