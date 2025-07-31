# QUESTÃO 1 DA P4 ANTECIPADA
# def contar_vogais_e_espacos(texto):
#     cont = 0

#     for c in texto:
#         if c in "AEIOU":
#             cont += 1

#     return cont
# print(contar_vogais_e_espacos("PrOgramAr é divertido"))


# QUESTÃO 2 DA P4 ANTECIPADA

# def inverter_palavras(frase):
#     if frase == "":
#         return ""
#     return inverter_palavras(frase[::-1])

# def inverter_palavra(frase):
#     saida = " "
#     for palavra in 

# QUESTÃO 3 DA P4 ANTECIPADA (recursiva)

# def subtrai_digitos(n):
#     if n < 10:
#         return n
#     s = str(n)
#     return int(s[0]) - soma_digitos(int(s[1:]))

# def soma_digitos(n):
#     if n < 10:
#         return n
#     s = str(n)
#     return int(s[0]) + soma_digitos(int(s[1:]))

# print(subtrai_digitos(1234))

# OU TAMBEM PODE SER RESOLVIDA DA SEGUINTE FORMA 

# def subtrai_digitos(n):
#     if n < 10:
#         return n

#     return subtrai_digitos(n//10) - n % 10

# print(subtrai_digitos(1234))

# QUESTÃO 4 DA P4 ANTECIPADA (recursiva)

# def remover_consoante_e_espacos(texto):
#     vogais  = "AEIOUYaeiouy"
#     if texto == "": # caso base é a string vazia 
#         return ""
    
#     if texto[0] in vogais:
#         return texto[0] + remover_consoante_e_espacos(texto[1:])
    
#     else:
#         return remover_consoante_e_espacos(texto[1:]) # remover consoante do restante 

# print(remover_consoante_e_espacos("python eh increvel"))