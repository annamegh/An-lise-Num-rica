import math

def pos_falsa(f, a, b, n, tol):
    fa, fb = f(a), f(b)
    if fa * fb >= 0:
        print("Não é possível usar o teorema de bolzano para determinar se essa função possui uma raiz nesse intervalo. Escolha outro intervalo.")
    else:
        for k in range(n):
            x1 = (a*f(b) - b*f(a)) / (f(b) - f(a))

            if abs(f(x1)) < tol:
                print(f"Encontrei uma raiz em x {k + 1}={x1}")
                return
            if f(a)*f(x1) < 0:
                a, b = a, x1
            if f(x1)*f(b) < 0:
                a, b = x1, b
    return 


func = lambda x: math.exp(3*x)-5
tol = 3.87187e-08
a = -0.947122
b = 1.121579
n = 100
pos_falsa(func, a, b, n, tol)