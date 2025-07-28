# Escreva uma função recursiva que receba uma string e retorne ela invertida.

def inverter(nome):
    if nome == "":
        return ""
    else:
        return nome[::-1]

texto = input()
resultado = inverter(texto)
print(resultado)
