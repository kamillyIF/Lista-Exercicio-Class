# Escreva uma função recursiva que verifique se uma string é palíndromo.

def palindromo(nome):
    return nome[::-1]
    
nome = input()    
resultado = palindromo(nome)
if nome == resultado:
    print("é palindromo")
else:
    print("não é palindromo")