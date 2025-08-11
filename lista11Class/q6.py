# Escreva um algoritmo que leia 10 numeros e os escreva em ordem decrescente.

numeros = []

for i in range(10):
    numero = int(input())
    numeros.append(numero)

numeros.sort(reverse = True)
print(numeros)