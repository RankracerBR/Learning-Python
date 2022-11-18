class Aluno:
    def __init__(self,nome='',matricula=0,notas=[]):#init inicializa o objeto(class)
        self.nome = nome 
        self.matricula = matricula 
        self.notas = notas 
    def __str__(self): #converte tudo para string
        return f'Nome: {self.nome}, Matrícula: {self.matricula}, Notas{self.notas}'
    def media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas) #média aritmética
        else:
            return 0