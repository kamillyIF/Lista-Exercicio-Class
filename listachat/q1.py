def  contar_vogais_minusculas(texto):
    vogais = "aeiou"
    cont = 0

    for letra in texto:
        if letra in vogais: # in verifica se esta dentro 
            cont += 1
    return cont
print (contar_vogais_minusculas("Estudar é muito bom"))