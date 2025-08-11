# Escreva um algoritmo que leia 30 n ́umeros inteiros e os armazene em uma lista. Escreva as
# funcoes maior, menor e soma. Elas devem receber a lista e retornar o respectivo valor. Por
# fim, faca chamadas as funções e imprima os retornos.

def maior(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def soma(lista):
    return sum(lista)

numeros = []
for i in range(5):
    num = int(input())
    numeros.append(num)

print("Maior número:", maior(numeros))
print("Menor número:", menor(numeros))
print("Soma dos números:", soma(numeros))