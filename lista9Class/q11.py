# Crie uma função chamada fatorial que calcule o fatorial de um número informado.
# Lembre-se que o fatorial de n é o produto de todos os inteiros positivos de 1 até n (exemplo: 5! = 5
# × 4 × 3 × 2 × 1).

def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1)

num = int(input())
resultado = fatorial(num)
print(resultado)