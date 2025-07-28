# Escreva uma função recursiva que receba um inteiro positivo com parametro
# e retorne a soma dos digitos

def soma(n):
    if n < 10:
        return n
    return n % 10 + soma(n//10)

num = int(input())
resultado = soma(num)
print(resultado)