#Escreva uma função recursiva que receba 2 interiros positivos, n e d, onde necessariamente
# o inteiro d possua apenas 1 digito. A função deve retorna o numero de ocorrencias de d em n.

def conta_digito(n, d):
    if n == 0:
        return 0  # CASO BASE: acabou o número, retorna 0
    ultimo = n % 10         # pega o último dígito
    resto = n // 10         # remove o último dígito
    if ultimo == d:
        return 1 + conta_digito(resto, d)  # se for igual, soma 1
    else:
        return conta_digito(resto, d)     # senão, só continua

n = int(input())
d = int(input())
resultado = conta_digito(n,d)
print(resultado)

