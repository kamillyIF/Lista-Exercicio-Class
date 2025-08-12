# Cremilda Chantilly é uma dentista e precisa  de ajuda para o gerenciamento de filas de atendimento.
# Desenvolva um programa que permita adicionar pacientes na fila e indique a vez do paciente a ser 
# atendido. Minimamente, disponibilize as funcionalidades de adicionar paciente e remover paciente.

def menu():
    print("1 - adicionar paciente regular")
    print("2 - remover paciente")
    print("3 - visualizar lista de pacientes")
    print("4 - sair")
    return input("opção: ")

def exibeFila(nome, fila):
    print(nome)
    if len(fila) == 0:
        print("fila vazia")
    else:
        for i in range(len(fila)):
            print(f"{i+1}. {fila[i]}")

def adicionar_paciente(fila):
    nome = input("Digite o nome do paciente: ")
    fila.append(nome)
    print(f"Paciente '{nome}' adicionado.")

def remover_paciente(fila):
    if len(fila) == 0:
        print("Não há pacientes na fila.")
    else:
        removido = fila.pop(0)
        print(f"Paciente '{removido}' foi removido da fila.")

fila = []
opc = menu()

while opc != "4":
    if opc == "1":
        adicionar_paciente(fila)
    elif opc == "2":
        remover_paciente(fila)
    elif opc == "3":
        exibeFila("Fila de pacientes:", fila)
    else:
        print("opção inválida")
    
    opc = menu()
