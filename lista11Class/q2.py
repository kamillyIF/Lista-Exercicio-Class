# Escreva um algoritmo que leia dois n ́umeros, limite inferior e limite superior, imprima
# o quadrado, x, de todos os n ́umeros de limite inferior a limite superior e, em seguida,
# imprima a soma dos n ́umeros impressos. Por exemplo, se o usu ́ario digitar 2 como limite
# inferior e 5 como limite superior, deve imprimir 4, 9, 16 e 25 e a soma 54. Armazene os
# valores que ser ̃ao impressos em uma lista e, para realizar a soma, crie uma fun ̧c ̃ao.

def soma(lista):
    return sum(lista)

quadrados = []

inferior = int(input()) # base
superior = int(input()) # expoente

for i in range(inferior,superior+ 1):
    num = i ** 2
    quadrados.append(num)

print(quadrados)
print(soma(quadrados))