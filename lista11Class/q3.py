# Escreva um algoritmo que imprima a lista dos 100 primeiros n ́umeros primos, iniciando do
# 2. N ́umero primo  ́e um n ́umero natural que tem apenas dois divisores diferentes, o 1 e ele
# mesmo. Por defini ̧c ̃ao, 1 n ̃ao e primo. Crie e utilize uma fun ̧c ̃ao que indica se um n ́umero
# e primo ou n ̃ao e mantenha os n ́umeros primos em uma lista. Imprima, ao final, a soma
# dos 100 n ́umeros primos impressos. Para isso, crie uma fun ̧c ̃ao chamada soma que receba
# a lista como parˆametro e retorne a soma.

# Função para verificar se um número é primo
def e_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def verificar_primo(qtd_primos):
    primos= []
    num = 2
    while len(primos) < qtd_primos:
        if e_primo(num):
            primos.append(num)
        num += 1
    return primos

def soma(lista):
    return sum(lista)

qtd_primos = 100
primos = verificar_primo(qtd_primos)
print("A soma dos 10 primeiros números primos é:", primos)



