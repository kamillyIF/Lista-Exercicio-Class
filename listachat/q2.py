
def inverter_palavra(frase):
    # Inicializa a variável de saída com um espaço em branco
    saida = ""
    
    # Divide a frase em palavras
    palavras = frase.split()
    
    # Itera sobre cada palavra
    for palavra in palavras:
        # Inverte a palavra e adiciona à saída
        saida += palavra[::-1] + " "
    
    # Retorna a frase sem o espaço extra no final
    return saida.strip()

# Testando a função
print(inverter_palavra("Python é divertido"))
