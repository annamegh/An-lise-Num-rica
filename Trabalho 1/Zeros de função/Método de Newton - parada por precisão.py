import math

def newton(f,df,x0,n,tol):
    raiz = x0
    for i in range(n):
        if df(raiz) != 0: # se a derivada for zero sai    
            raiz=raiz-f(raiz)/df(raiz)
        else:
            print(f"Divisão por zero em x_{i + 1}={raiz}")
        if abs(f(raiz)) < tol:
            print(f"Encontrei uma raiz em x_{i + 1}={raiz}")
            return

    return 

# teste :

func = lambda x: math.exp(3*x)-5
x_0 = 1.535352
df= lambda x: 3*math.exp(3*x)
tol = 3.87187e-08
n = 100
newton(func,df, x_0, n, tol)