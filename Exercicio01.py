from ListaDupla import ListaDupla
from ListaDupla import No

def printar(lista):
    cont = 0
    aux = lista.inicio
    
    while cont < lista.tamanho:
        print(aux.dado, end=' ')
        aux = aux.dir
        cont += 1

def apontar_inicio(lista):
    aux = lista.inicio
    
    if lista.tamanho > 1:
        aux.esq = lista.fim # A função já aponta para o dir, então só apontamos o fim
        
def apontar_final(lista):
    aux = lista.fim
    
    if lista.tamanho > 1:
        aux.dir = lista.inicio # A função já aponta para o esq, então só apontamos o início
        
def inserir(lista):
    aux = lista.inicio
    
    dado = int(input('Informe o valor --> '))
    posi = int(input('Informe a posição --> '))
    
    if posi > lista.tamanho:
        lista.add_final(dado)
        apontar_final(lista) # Aponta para o início
        apontar_inicio(lista) # O início aponta para o novo final
    elif posi == 1:
        lista.add_inicio(dado)
        apontar_inicio(lista) # Aponta para o final
        apontar_final(lista) # O final aponta para o novo início
    else:
        for _ in range(posi - 1):
            aux = aux.dir
            
        novo = No(dado) # Transformando o novo em nó
        
        aux.esq.dir = novo
        novo.esq = aux.esq
        novo.dir = aux
        aux.esq = novo
        lista.tamanho += 1 # Aumenta o tamanho da lista depois de por um novo

def gerar_menu():
    print()
    print('[1] Inserir um dado no final da lista')
    print('[2] Inserir um dado em uma posição desejada')
    print('[3] Remover algum dado da lista')
    print('[4] Imprimir lista')
    print('[5] Finalizar')
    print()

def main():
    lista = ListaDupla()
    
    while True:
        gerar_menu()
        opcao = int(input('Informe uma opção --> '))
        
        match opcao:
            case 1:
                n = int(input('Informe um valor --> '))
                lista.add_final(n)
                apontar_final(lista)
                apontar_inicio(lista)
            case 2:
                inserir(lista)
            case 3:
                n2 = int(input('Informe um valor --> '))
                lista.remover(n2)
            case 4:
                printar(lista)
            case 5:
                print('Finalizado!')
                break
            case _:
                print('Informe uma opção válida')
    
if __name__ == '__main__':
    main()
