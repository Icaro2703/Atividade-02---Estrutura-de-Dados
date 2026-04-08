# Tem muito if mas eu usei a ideia do ex1 de usar for... rsrs

from ListaDupla import ListaDupla
from Paciente import Paciente
from ListaDupla import No

prio = 0

def inserir(lista):
    aux = lista.inicio
    global prio
    
    nome = input('Informe o nome do paciente --> ')
    prioridade = int(input('Informe a prioridade --> 0 - Comum | 1 - Prioritário '))
    
    novo = No(Paciente(nome, prioridade)) # Transformando o paciente em um novo nó
    
    if prioridade == 0:
        lista.add_final(Paciente(nome, prioridade))
    elif prioridade == 1:
        if prio == 0: # Se for o primeiro, bota no início
            lista.add_inicio(Paciente(nome, prioridade))      
            prio += 1 # Aumenta +1 pq não cai no caso lá embaixo no else
        else:
            if prio == 1 and aux.dir is None: # Se houver só um prioritário, sem nada depois
                aux.dir = novo
                novo.esq = aux
                novo.dir = None
            elif prio == 1 and aux.dir is not None: # Só um prioritário mas tem algo depois
                aux.dir.esq = novo
                novo.dir = aux.dir
                aux.dir = novo
                novo.esq = aux
            else:       
                for _ in range(prio - 1): # Se tiver mais de um, percorre
                    aux = aux.dir
                        
                if aux.dir is not None: # Existe um próximo
                    aux.dir.esq = novo
                    novo.dir = aux.dir
                    aux.dir = novo
                    novo.esq = aux
                            
                elif aux.dir is None: # Não existe um próximo
                    aux.dir = novo
                    novo.esq = aux
                    novo.dir = None
                    
            lista.tamanho += 1
            prio += 1

def atender(lista):
    aux = lista.inicio
    global prio
    
    if lista.tamanho == 0:
        print('Não há pacientes para serem atendidos')
    else:
        print(f'Paciente a ser atendido: {aux.dado}')
    
        lista.remover(aux.dado)
        
        if aux.dado.prioridade == 1: # Se remover um prioritário diminui a variável
            prio -= 1
    
def buscar(lista):
    nome = input('Informe o nome do paciente: ')
    aux = lista.inicio
    cont = 0
    
    while aux:
        if aux.dado.nome == nome: # Se aux.paciente.nome for o nome
            print(aux.dado, end='\n') # Printa o paciente e a prioridade
            cont = 1
        aux = aux.dir
    if cont == 0:
        print('Paciente não encontrado.')
        print()

def gerar_menu():
    print()
    print('[1] Inserir novo paciente')
    print('[2] Atender o próximo paciente')
    print('[3] Imprimir lista de pacientes')
    print('[4] Buscar paciente')
    print('[5] Finalizar')
    print()

def main():
    lista = ListaDupla()
    
    while True:
        gerar_menu()
        opcao = int(input())
        print()
        
        match opcao:
            case 1:
                inserir(lista)
            case 2:
                atender(lista)
            case 3:
                lista.imprimir()
            case 4:
                buscar(lista)
            case 5:
                print('Finalizando sessão...')
                break
            case _:
                print('Número inválido')
    
    
if __name__ == '__main__':
    main()
    