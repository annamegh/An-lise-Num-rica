import math

def secante(f,x_0, x_1, n, tol):
    
    raiz = x_0
    for i in range(n):
        if f(x_0) - f(x_1) != 0:   
            raiz= (x_0*f(x_1) - x_1*f(x_0)) / (f(x_1) - f(x_0))
        else:
            print(f"Divisão por zero em x_{i + 1}={raiz}")
        if abs(f(raiz)) < tol:
            print(f"Encontrei uma raiz em x {i + 1}={raiz}")
            return
        
        x_0 = x_1
        x_1 = raiz
    return 

# teste :

func = lambda x: math.exp(3*x)-5
tol = 3.87187e-08
x0 = -0.496986
x1 = 1.361031
n = 100
secante(func, x0, x1, n, tol)