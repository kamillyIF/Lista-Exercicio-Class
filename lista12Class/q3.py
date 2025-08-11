# Escreva um algoritmo que leia uma matriz 2 x 2. 
# Em seguida, deve calcular e imprimir o determinante.

print("Digite os elementos da matriz 2x2:")

a = int(input("Elemento [0][0]: "))
b = int(input("Elemento [0][1]: "))
c = int(input("Elemento [1][0]: "))
d = int(input("Elemento [1][1]: "))

determinante = a * d - b * c

print(f"O determinante da matriz é: {determinante}")