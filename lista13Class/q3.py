# Desenvolva uma v2 para o programa das filas. Desta vez ele deve manter 2 filas, uma para atendimentos
# regulares e outra para prioridades. No atendimento começar pela prioridade,  se houver, e em seguida
# ir alternando, ou seja,  um prioridade, um regular, outro prioridade e outro regular, até o final 
# das filas.

fila_prioridade = []
fila_regular = []

def adicionar_paciente(nome, prioridade=False):
    if prioridade:
        fila_prioridade.append(nome)
        print(f"Paciente '{nome}' adicionado na fila PRIORITÁRIA.")
    else:
        fila_regular.append(nome)
        print(f"Paciente '{nome}' adicionado na fila REGULAR.")

def atender_pacientes():
    print("\nInício do atendimento alternado:")
    i = 0
    while fila_prioridade or fila_regular:
        if i % 2 == 0:  # vez da fila prioridade
            if fila_prioridade:
                paciente = fila_prioridade.pop(0)
                print(f"Atendendo PRIORITÁRIO: {paciente}")
            elif fila_regular:
                paciente = fila_regular.pop(0)
                print(f"Atendendo REGULAR: {paciente}")
        else:  # vez da fila regular
            if fila_regular:
                paciente = fila_regular.pop(0)
                print(f"Atendendo REGULAR: {paciente}")
            elif fila_prioridade:
                paciente = fila_prioridade.pop(0)
                print(f"Atendendo PRIORITÁRIO: {paciente}")
        i += 1

# Simulação
adicionar_paciente("Ana", prioridade=True)
adicionar_paciente("Carlos")
adicionar_paciente("Beatriz", prioridade=True)
adicionar_paciente("Diego")
adicionar_paciente("Eduardo")

atender_pacientes()
