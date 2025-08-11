# Tuconaldo Tripa é mecânico e anda meio broco. Precisa de sua ajuda. 
# Desenvolva um programa que receba os nomes das peças que ele está removendo,
# na ordem, e depois vá indicando, uma a uma,  na ordem inversa da adição, as 
# peças para remontar o carro. Operações adicionar peça e remover peça.

pilha = []  # lista vazia representando a pilha

# função para adicionar peça
def adicionar_peca(nome):
    pilha.append(nome)
    print(f"Peça '{nome}' adicionada.")

# função para remover peça (para remontar)
def remover_peca():
    if len(pilha) == 0:
        print("Não há peças para remover.")
        return None
    p = pilha.pop()
    print(f"Peça '{p}' removida para remontar.")
    return p

# Simulação

# Adicionando peças (removidas do carro)
adicionar_peca("Parafuso")
adicionar_peca("Filtro de óleo")
adicionar_peca("Correia")

print("\nHora de remontar o carro...")

# Removendo peças na ordem inversa para remontar
remover_peca()
remover_peca()
remover_peca()
remover_peca()  # testando remover peça quando pilha está vazia
