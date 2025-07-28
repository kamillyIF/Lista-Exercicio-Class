# Dizemos que um natural (inteiro positivo), n, é um quadrado perfeito se sua raiz quadrada
# é também um número natural. Crie uma função chamada verifica_quadrado_perfeito que recebe um
# número e retorna informando se ele é, ou não é, um quadrado perfeito.

import math

def verifica_quadrado_perfeito(n):
    if n < 0:
        return "não é quadrado perfeito"
    
    raiz = int(math.sqrt(n)) # calcula a raiz e tranforma em um inteiro 

    return raiz * raiz == n # se raiz ao quadrado for igual a n, é quadrado perfeito