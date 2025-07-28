# Crie uma função chamada calculadora que receba três parâmetros: dois números e uma
# operação (um caractere: "+", "-", "*", "/"). A função deve realizar a operação matemática
# correspondente e retornar o resultado.

def calculadora(num1,num2,operacao):
    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        return num1 / num2

# PARA O USUARIO DIGITAR
# n1 = int(input())
# n2 = int(input())
# operacao = input()
# resultado = calculadora(n1,n2,operacao)
# print(resultado)