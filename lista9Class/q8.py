# Crie uma função chamada potencia que receba dois parâmetros, base e expoente, e
# retorne o resultado da base elevada ao expoente.

def potencia(base,expoente):
    return base ** expoente

n1 = int(input())
n2 = int(input())
resultado = potencia(n1,n2)
print(resultado)

# utilizando pow

# def potencia(base,expoente):
#     return pow(base,expoente)