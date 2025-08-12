# Tuconaldo Tripa é mecânico e anda meio broco. Precisa de sua ajuda. 
# Desenvolva um programa que receba os nomes das peças que ele está removendo,
# na ordem, e depois vá indicando, uma a uma,  na ordem inversa da adição, as 
# peças para remontar o carro. Operações adicionar peça e remover peça.

def menu():
    print("1 - adicionar peça")
    print("2 - remover peça")
    print("3 - visualizar lista de peça")
    print("4 - sair")
    return input("opção: ")

def exibeFila(nome, fila):
    print(nome)
    if len(fila) == 0:
        print("fila vazia")
    else:
        for i in range(len(fila)):
            print(f"{i+1}. {fila[i]}")

def adicionar_peca(fila):
    nome = input("digite o nome da peça: ")
    fila.append(nome)

def remover_peca(fila):
    if len(fila) == 0:  
        print("não ha peça na fila")
    else:
        removido = fila.pop()
        print(f"a peça '{removido}' foi removida.")

fila = []
opc = menu()

while opc != "4":
    if opc == "1":
        adicionar_peca(fila)
    elif opc == "2":
        remover_peca(fila)
    elif opc == "3":
        exibeFila("lista das peças",fila)
    else:
        print("opção invalida")

    opc = menu()
