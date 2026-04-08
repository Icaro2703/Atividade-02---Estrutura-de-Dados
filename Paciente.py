from ListaDupla import ListaDupla

class Paciente:
    def __init__(self, nome: str, prioridade: int = 0):
        self.nome = nome
        self.prioridade = prioridade

        
    # Ao printar o objeto, não vem o end de memória, e sim essa string, com nome e prioridade
    def __str__(self):
        tipo = ''
        if self.prioridade == 0:
            tipo = 'Comum'
        else:
            tipo = 'Prioritário'
        
        return f'Nome: {self.nome} | Prioridade: {tipo}\n'