# Escreva um algoritmo que leia um inteiro  n e uma matriz de dimensão escolhida pelo usuário. 
# Em seguida, deve calcular e escrever o resultado do produto escalar.

def produto_escalar(v1, v2):
    if len(v1) != len(v2):
        print("Vetores de tamanhos diferentes!")
        return None
    soma = 0
    for i in range(len(v1)):
        soma += v1[i] * v2[i]
    return soma

n = int(input("Digite o tamanho dos vetores: "))

print("Digite os elementos do primeiro vetor:")
v1 = [int(input()) for _ in range(n)]

print("Digite os elementos do segundo vetor:")
v2 = [int(input()) for _ in range(n)]

resultado = produto_escalar(v1, v2)

if resultado is not None:
    print(f"Produto escalar: {resultado}")
