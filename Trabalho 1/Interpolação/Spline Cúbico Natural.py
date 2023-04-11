import numpy as np
import math

def spline( x, y):
    n = len(x)
    a = {k:v for k, v in enumerate(y)}
    h = {k: x[k+1] - x[k] for k in range(n-1)}

    A = [[1] + [0] * (n-1)]
    for i in range(1, n-1):
        row = [0] * n
        row[i - 1] = h[i-1]
        row[i] = 2*(h[i-1] + h[i])
        row[i+1] = h[i]
        A.append(row)
    A.append([0] * (n-1) + [1])

    B = [0]
    for k in range(1, n-1):
        row = 3* (a[k+1] - a[k]) / h[k] - 3 * (a[k] - a[k-1]) / h[k-1]
        B.append(row)
    B.append(0)
    c = dict(zip(range(n), np.linalg.solve(A,B)))
    
    b = {}
    d = {}
    for k in range(n - 1):
        b[k] = (1/h[k]) * (a[k+1] - a[k]) - (h[k]/3) * (2*c[k] + c[k+1])
        d[k] = (c[k+1] - c[k])/(3*h[k])

    s = {}
    
    for k in range(n-1):
        eq = [a[k], b[k], c[k], d[k]]
        #eq = lambda X: a[k] + b[k]*(X - x[k]) + c[k]*(X - x[k])**2 + d[k]*( X - x[k])**3
        s[k] = {'eq': eq, 'domain': [x[k], x[k+1]]}

    return s

"""
#ENCONTRAR OS COEFICIENTES a, b, c, d
x = [-2.492, 0.018, 2.221, 4.163]
y = [2.612, 4.506, 2.094, 2.246]

coefs = spline(x, y)
for k in range(len(coefs)):
    e = coefs[k].get('eq')
    for i in range(len(e)):
        print(e[i], ',')
"""


"""
#ENCONTRAR OS COEFS a, b, c e d, NÃO TENDO Y
x = [-0.387, -0.186, -0.058, 0.079, 0.213, 0.387, 0.572, 0.76, 0.886, 1.018, 1.273, 1.431]
f = lambda x: x**5 - 4*x**2 + 2*math.sqrt(x+1) + math.cos(x)

y = []

for i in range(len(x)):
    y.append(f(x[i]))

eqs = spline(x, y)
for k in range(len(eqs)):
    e = eqs[k].get('eq')
    for i in range(len(e)):
        print(e[i], ',')
"""

"""
#CALCULAR S(X)
x = [0.247, 0.47, 0.767, 1.057, 1.457, 1.729, 2.163, 2.534, 2.841, 3.181, 3.581, 3.868]
y = [1.176, 1.051, 2.025, 1.935, 2.274, 2.171, 2.621, 1.466, 0.832, 0.587, 1.245, 2.79]
valores = [0.451, 0.647, 1.926, 2.017, 3.276]

eqs = spline(x, y)

for i in range(len(valores)):
    for k in range(len(eqs)):
        a = eqs[k].get('eq')
        b = eqs[k].get('domain')

        f = lambda x: a[0] + a[1]*(x - b[0]) + a[2]*(x - b[0])**2 + a[3]*(x - b[0])**3
        
        if (valores[i] >= b[0]) & (valores[i] <= b[1]):
            print(f(valores[i]), ',')
"""