# Escreva um algoritmo que leia as 4 m´edias bimestrais para cada um dos 40 alunos de uma
# turma. Em seguida, deve se calcular e imprimir a m´edia anual de cada aluno e a m´edia
# anual da turma. Mantenha as m´edias todas em uma lista, estrutura que deve ser criada
# ao longo da entrada. Crie m´etodos, a sua escolha, para usar durante o processamento dos
# dados.

alunos = 40
media_anuais = []

for i in range(alunos):
    notas = []
    for j in range(4):
        nota = float(input())
        notas.append(nota) # adicionar notas ao final da fila
    media_anual = sum(notas) / 4
    media_anuais.append(media_anual)
    print(f"{media_anual:.2f}")

media_turma = sum(media_anuais) / alunos
print(f"{media_turma:.2f}")