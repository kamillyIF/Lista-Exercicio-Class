# Escreva um algoritmo que leia 2 matrizes,  calcule e escreva o produto
# delas. O  algoritmo deve permitir matrizes de diversas dimensões e deve 
# validar se é possível calcular.

def produto_matrizes(A, B):
    # Verifica se o produto é possível
    if len(A[0]) != len(B):
        print("Produto impossível: número de colunas de A diferente do número de linhas de B.")
        return None
    
    m = len(A)
    n = len(A[0])  # ou len(B)
    q = len(B[0])

    # Inicializa a matriz resultado com zeros
    C = [[0 for _ in range(q)] for _ in range(m)]

    # Calcula o produto
    for i in range(m):
        for j in range(q):
            soma = 0
            for k in range(n):
                soma += A[i][k] * B[k][j]
            C[i][j] = soma
    return C

# Exemplo de uso
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

resultado = produto_matrizes(A, B)
if resultado:
    print("Resultado do produto das matrizes:")
    for linha in resultado:
        print(linha)
