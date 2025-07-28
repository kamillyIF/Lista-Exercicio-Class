# Escreva uma função recursiva em Python que calcule ab (a elevado à potência b), sendo a e b
# inteiros positivos.

def potencia(a,b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b - 1)
    
n1 = int(input())
n2 = int(input())
resultado = potencia(n1,n2)
print(resultado)