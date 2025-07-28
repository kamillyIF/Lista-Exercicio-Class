# Crie uma função chamada inverter_string que receba uma string como argumento e
# retorne a string invertida.
# [::-1] significa: "pegue tudo da string, de trás para frente".

def inverter_string(texto):
    return texto[::-1] # inverte toda string
    
string = input()
resultado = inverter_string(string)
print(resultado)