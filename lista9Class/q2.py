# Crie uma função chamada par_ou_impar que receba um número inteiro como parâmetro e
# retorne "Par" se o número for par e "Ímpar" se o número for ímpar.

def par_ou_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "impar"