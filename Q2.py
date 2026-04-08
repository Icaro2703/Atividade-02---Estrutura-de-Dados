class No:
    def __init__(self, nome, tempo):
        self.nome = nome
        self.tempo = tempo
        self.tempo_espera = 0
        self.tempo_retorno = 0
        self.tempo_aux = tempo
        self.dir = None
        self.esq = None

class Aria:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        self.media_espera = 0
        self.media_retorno = 0
        
    def inserir(self, nome, tempo):
        novo = No(nome, tempo)
        
        if self.tamanho == 0:
            self.inicio = novo
            self.fim = novo
            self.fim.dir = novo
            self.inicio.esq = novo
        
        else:
            self.inicio.esq = novo
            self.fim.dir = novo
            novo.esq = self.fim
            self.fim = novo
            self.fim.dir = self.inicio
        
        self.tamanho += 1
        
    def executar(self, unid_tempo):
        lista_processos_finalizados = []
        cont = self.tamanho
        tempo_total = 0
        aux = self.inicio
        while self.tamanho != 0:
            if aux.tempo - unid_tempo <= 0:
                tempo_total += aux.tempo
                aux.tempo_retorno = tempo_total
                aux.tempo_espera = aux.tempo_retorno - aux.tempo_aux
                self.media_espera += aux.tempo_espera
                self.media_retorno += aux.tempo_retorno
                lista_processos_finalizados.append(aux)
                aux = aux.dir
                self.remover(aux.esq.nome)
            else:
                tempo_total += unid_tempo
                aux.tempo -= unid_tempo
                aux = aux.dir

        self.media_espera = self.media_espera / cont
        self.media_retorno = self.media_retorno / cont
        self.gerar_relatorio(unid_tempo, lista_processos_finalizados)
         
    def remover(self, nome):
        aux = self.inicio
        
        for i in range(self.tamanho):
            if aux.nome == nome:
                if i == 0:
                    aux.dir.esq = self.fim
                    self.fim.dir = aux.dir
                    self.inicio = aux.dir
                    aux.dir = None
                    aux.esq = None
                
                elif i == (self.tamanho - 1):
                    aux.esq.dir = self.inicio
                    self.inicio.esq = aux.esq
                    self.fim = aux.esq
                    aux.dir = None            
                    aux.esq = None    
                
                else:
                    aux.dir.esq = aux.esq
                    aux.esq.dir = aux.dir
                    aux.dir = None
                    aux.esq = None
                    
                self.tamanho -= 1
                break

            aux = aux.dir   

    def gerar_relatorio(self, unid_tempo, lista):
        print()
        print("RELATÓRIO FINAL - ARIA Recovery Module")
        print("-"*80)
        print(f"Fatia de tempo (quantum): {unid_tempo} unidades")
        print("-"*80)
        print(f"{'Processo':<15} {'Tempo total':<15} {'Tempo de espera':<20} {'Tempo retorno':<20}")
        for processo in lista:
            print(f"{processo.nome:<20} {processo.tempo_aux:<15} {processo.tempo_espera:<20} {processo.tempo_retorno:<20}")
        print("-"*80)
        print(f"{'Média':<20} {'-':<15} {self.media_espera:<20} {self.media_retorno:<20}")

# Programa principal
print()
processos = int(input("Quantos processos serão feitos? "))
unid_tempo_cpu = int(input("Em quantas unidades de tempo a CPU executa cada processo? "))
lista = Aria()
print()

for i in range(processos):
    nome = input(f"Qual o nome do {i + 1}º processo? ")
    tempo = int(input("Quantas unidades de tempo ele leva para ser executado? "))
    lista.inserir(nome, tempo)
    print()

lista.executar(unid_tempo_cpu)
