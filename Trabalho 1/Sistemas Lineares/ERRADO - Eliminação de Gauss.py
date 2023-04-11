import numpy as np

def eliminacao(A, B):
    s = np.linalg.solve(A,B)


def gauss (E):
    l = len(E)
    c = len(E[0])
    for j in range(c-2):
       for i in range(j,l):
            if(E[i][j] != 0):
                if(i != j):
                    for k in range(c):
                        temp = E[i][k]
                        E[i][k] = E[j][k]
                        E[j][k] = temp
                for m in range(j+1,l):
                    a = -E[m][j]/E[j][j]
                    for n in range(j,c):
                        E[m][n] += a*E[j][n] 
                print_matriz(E)
            break
    return

def print_matriz(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end="\t")
        print('')
    print('')
    return

E = [[2,4,6,2,4],
     [1,2,-1,3,8],
     [-3,1,-2,1,-2],
     [1,3,-2,-2,6]
]
print_matriz(E)
gauss(E)
