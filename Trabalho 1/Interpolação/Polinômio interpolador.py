import numpy as np
import math
#import matplotlib.pyplot as plt

def interpolate(x: list, y: list) -> list:
    A = []
    n = len(x)
    for xi in x:
        row = []
        for deg in range(n):
            if deg == 0:
                row.append(1)
            else:
                row.append(xi ** deg)
        A.append(row)
    B = y
    return np.linalg.solve(A, B)


def build_poly(coeffs):
    """
    Constrói uma função a partir dos coeficientes
    """
    def poly(x):
        soma = coeffs[0]
        soma += sum(ck * x**k for k, ck in enumerate(coeffs[1:],1))
        return soma
    return poly


#ACHAR OS COEFICIENTES DADOS 3 PONTOS
x = [0.361, 0.961, 1.505, 2.128, 2.614, 3.079, 3.702, 4.184, 4.93, 5.411, 6.277, 6.767]
y = [4.349, 4.789, 4.922, 4.698, 4.276, 3.747, 3.012, 2.553, 2.213, 2.258, 2.68, 2.939]
coefs = interpolate(x, y)
for i in range(len(coefs)):
    print(coefs[i],',')


"""
#ACHAR OS COEFICIENTES DADA UMA FUNÇÃO E OS VALORES EM X
f = lambda x: 1/(1 + 25*x**2)

x = [-0.857, -0.767, -0.61, -0.425, -0.189, 0.017, 0.155, 0.387, 0.549, 0.768, 0.857]
y = [f(x[0]), f(x[1]), f(x[2]), f(x[3]), f(x[4]), f(x[5]), f(x[6]), f(x[7]), f(x[8]), f(x[9]), f(x[10])]

coefs = interpolate(x, y)
for i in range(len(coefs)):
    print(coefs[i],',')
"""

"""
#ACHAR OS COEFS E CALCULAR O VALOR DE Y PARA A FUNÇÃO ENCONTRADA
x = [-1.168, -0.482, 0.295, 1.304, 2.614, 3.553, 4.526, 5.11, 6.628]
y = [0.852, 0.965, 0.975, 0.808, -0.017, -0.737, -0.989, -0.767, 0.546]

coefs = interpolate(x, y)
f = build_poly(coefs)

values = [-1.041, -0.595, 0.906, 1.144]

for i in range(len(values)):
    print(f(values[i]), ',')
"""

"""
#ACHAR O ERRO ABSOLUTO: ACHAR OS COEFICIENTES DADA UMA FUNÇÃO E OS VALORES EM X, CALCULAR O VALOR DE X PELO POLINOMIO CRIADO
# |f(x) - p(x)|
f = lambda x: math.exp(-x**2) + math.cos(x) + 3
x = [0.341, 0.907, 1.636, 2.803, 3.551, 4.291, 4.82, 6.048, 6.788]
values = [1.719, 5.536, 5.76, 5.852, 5.896]

y = []
for i in range(len(x)):
    y.append(f(x[i]))

coefs = interpolate(x, y)
p = build_poly(coefs)

for i in range(len(values)):
    print(abs(f(values[i]) - p(values[i])), ',')
"""