# Escreva um algoritmo que leia 10 nomes e os escreva em ordem alfab´etica.

nomes = []
for i in range(10): # le os 10 nomes 
    nome = input()
    nomes.append(nome) #adiciona os nomes no final da fila

nomes.sort() #ordenar a lista 
print("Ordem alfabetica")
for nome in nomes:
    print(nome)
