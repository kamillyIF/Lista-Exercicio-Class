# Cremilda Chantilly é uma dentista e precisa  de ajuda para o gerenciamento de filas de atendimento.
# Desenvolva um programa que permita adicionar pacientes na fila e indique a vez do paciente a ser 
# atendido. Minimamente, disponibilize as funcionalidades de adicionar paciente e remover paciente.

fila = []

def adicionar_paciente(nome):
    fila.append(nome)
    print(f"Paciente '{nome}' adicionado na fila.")

def atender_paciente():
    if len(fila) == 0:
        print("Não há pacientes na fila.")
        return None
    paciente = fila.pop(0)
    print(f"Paciente '{paciente}' está sendo atendido.")
    return paciente

# Simulação

adicionar_paciente("João")
adicionar_paciente("Maria")
adicionar_paciente("Carlos")

atender_paciente()
atender_paciente()
atender_paciente()
atender_paciente()  # fila vazia
