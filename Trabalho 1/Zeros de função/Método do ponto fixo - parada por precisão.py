import math

def ponto_fixo(f, x0, n, tol):
    for i in range(n):
        x = f(x0)
        if abs(f(x)) < tol:
            print(f"{x},")
            return
        x0 = x

    return

func = lambda x: math.sqrt((x + 3) / (pow(x, 2) + 2))
x0 = 1.6635
tol = 3.0
n = 100
ponto_fixo(func, x0, n, tol)