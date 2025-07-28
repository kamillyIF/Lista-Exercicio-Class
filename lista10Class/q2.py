# Escreva uma função recursiva em Python que receba o primeiro termo (a1), a razão e o
# número de elementos, n, de uma Progressão Aritmética (PA) e, em seguida, calcule e retorne
# o resultado da soma dos termos da PA.

def recursiva(a1,r,n):
    if n == 1:
        return a1
    else:
        return a1 + recursiva(a1 + r, r, n - 1)


