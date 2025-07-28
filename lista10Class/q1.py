# 1. A série de Fibonacci tem 0 como primeiro e 1 como segundo elemento. A partir daí, a série
# segue definindo o próximo valor como a soma dos dois anteriores. Por exemplo, o terceiro
# elemento da série é 1 e o quarto é 2. Os oito primeiros elementos são 0, 1, 1, 2, 3, 5, 8 e 13.
# Escreva uma função que receba um número inteiro, i, e retorne o i-ésimo elemento da série.
# Em seguida escreva um programa que leia números inteiros e indique os i-ésimos números
# da série, usando a função. O programa deve ser encerrado quando a entrada for -1.

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    return fibonacci(i-1) + fibonacci(i-2)

n = int(input())
resultado = fibonacci(n + 1) # o + 1 pega n tambem 
for j in range(n):
    print(fibonacci(j), end = ' ') #end separa por espaço