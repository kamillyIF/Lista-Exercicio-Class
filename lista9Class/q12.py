# Crie uma função chamada verifica_palindromo que recebe uma string como parâmetro e
# informa se a palavra é um palíndromo.

def verificar_palindromo(palavra): # palindromo - Quando ela é lida de tras para frente é igual à original
    palavra = palavra.lower() # deixa tudo minuscul0
    invertida = palavra[::-1] # inverte a string

string = input()
resultado = verificar_palindromo(string)
print(resultado)
