import numpy as np
import math

def divided_differences( x, y):
    Y = [item for item in y]
    coeffs = [y[0]]
    n = len(y)
    for i in range(n - 1):
        coeffs.append(0)
        for j in range(n - 1 - i):
            numer = Y[j+1] - Y[j]
            denom = x[j+1+i] - x[j]
            Y[j] = numer/ denom
        coeffs[i + 1] = Y[0]
    return coeffs

def eq(x, coeffs):
    n = len(x)
    equation = ''
    for i in range(n):
        equation += f'{coeffs[i]:+}' + '*'.join([f'(x{-xj:+})' for j, xj in enumerate(x) if j < i])
    return equation

"""
#ENCONTRAR COEFICIENTES A PARTIR DE UMA FUNÇÃO E DAS COORDENADAS X DOS PONTOS
x = [-2.644, -2.267, -1.805, -1.193, -0.683, -0.172, 0.176, 0.807, 1.228, 1.652, 2.169, 2.828, 3.07, 3.585, 4.306]

f = lambda x: math.cos(x)**3 + 2*math.cos(x)**2 + 1
y = []

for i in range(len(x)):
    y.append(f(x[i]))

coefs = divided_differences(x, y)

for i in range(len(coefs)):
    print(coefs[i], ',')
"""