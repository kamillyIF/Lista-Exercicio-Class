# Crie uma função chamada verificar_primo que receba um número inteiro e retorne True
# se o número for primo e False caso contrário.

def verificar_primo(n):
    if n <= 1:
        return False
    for i in range(2,n): # testa os numeros de 2 ate 1
        if n % i == 0: # se encontrar algum divisor não é primo (retorna falso)
            return False
        
    return True


num = int(input())
resultado = verificar_primo(num)
print(resultado)