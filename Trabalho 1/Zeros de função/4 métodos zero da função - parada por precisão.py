import math
def bisection(f, a, b, n, tol):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        print("Não é possível usar o teorema de bolzano para determinar se essa função possui uma raiz nesse intervalo. Escolha outro intervalo.")
    else:
#        n = max(lista)
        for k in range(n):
            m = 0.5 * (a + b)
#            if (k + 1) in lista:
#                print(f"{m},")
            fm = f(m)
            if abs(fm) < tol:
                print(f"b {k + 1}, {m},")
                return
            if fa * fm < 0:
                b = m
            else:
                a = m
        return

def newton(f,df,x0,n,tol):
    raiz = x0
    for i in range(n):
        if df(raiz) != 0: # se a derivada for zero sai    
            raiz=raiz-f(raiz)/df(raiz)
        else:
            print(f"Divisão por zero em x_{i + 1}={raiz}")
        if abs(f(raiz)) < tol:
            print(f"n {i + 1}, {raiz},")
            return

    return 



def secante(f,x_0, x_1, n, tol):
    
    raiz = x_0
    for i in range(n):
        if f(x_0) - f(x_1) != 0:   
            raiz= (x_0*f(x_1) - x_1*f(x_0)) / (f(x_1) - f(x_0))
        else:
            print(f"Divisão por zero em x_{i + 1}={raiz}")
        if abs(f(raiz)) < tol:
            print(f"s {i + 1}, {raiz},")
            return
        
        x_0 = x_1
        x_1 = raiz
    return 

def pos_falsa(f, a, b, n, tol):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        print("Não é possível usar o teorema de bolzano para determinar se essa função possui uma raiz nesse intervalo. Escolha outro intervalo.")
    else:
        for k in range(n):
            x1 = (a*f(b) - b*f(a)) / (f(b) - f(a))

            if abs(f(x1)) < tol:
                print(f"p {k + 1}, {x1},")
                return
            if f(a)*f(x1) < 0:
                a, b = a, x1
            if f(x1)*f(b) < 0:
                a, b = x1, b
    return 

func = lambda x:  math.log(x**2 + 2) * math.exp(math.pi - x) - 3
tol = 1.11939e-08
df = lambda x: math.exp(math.pi - x)*( 2*x - (x**2 +2)*math.log(x**2 + 2))/(x**2 + 2)
n = 500000

bisection(func, 1.012517, 4.713837, n, tol)
newton(func, df, 9.960912, n, tol)
secante(func, -2.612666, 6.194602, n, tol)
pos_falsa(func, -4.911568, 4.506062, n, tol)

