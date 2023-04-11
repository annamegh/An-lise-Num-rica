import numpy as np
import math

def lagrange(x: list, y: list) -> list:
    # a lista coeffs contém y_i / denom_i
    # onde denom_i é o denominador de L_i
    n = len(x)
    coeffs = []
    for i in range(n):
        denom_i = np.prod([x[i] - x[j] for j in range(n) if j != i])
        coeffs.append(y[i] / denom_i)
    return coeffs
def build_poly(x, coeffs):
    n = len(x)
    def poly(t):
        comb = 0
        for i in range(n):
            numer = 1
            for j in range(n):
                if j != i:
                    numer *= (t - x[j])
            numer *= coeffs[i]
            comb += numer
        return comb
    return poly

"""
x = [1.568, 1.806, 2.194, 2.354, 2.654, 3.083, 3.29, 3.703, 3.979, 4.289, 4.652, 4.786]
y = [-0.811, -0.969, -0.954, -0.867, -0.614, -0.128, 0.121, 0.572, 0.801, 0.959, 0.993, 0.963]
coeffs = lagrange(x, y)

for i in range(len(coeffs)):
    print(coeffs[i], ',')
"""

#ACHAR OS COEFS DADA UMA FUNÇÃO E OS PONTOS EM X

x = [0.345, 0.52, 0.734, 1.039, 1.108, 1.358, 1.657, 1.885, 2.018, 2.206, 2.523, 2.692, 2.931]
func = lambda x:  math.cos(math.sin(math.log(x**2)))

y = []
for i in range(len(x)):
    y.append(func(x[i]))

coeffs = lagrange(x, y)

for i in range(len(coeffs)):
    print(coeffs[i], ',')