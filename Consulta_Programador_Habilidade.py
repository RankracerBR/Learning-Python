from Programador_Habilidade_tabela_ import Programadores

#Insere dados na tabela pessoa
def insere_programador():
    programador = Programadores(nome='Julia',idade=19)
    print(programador)
    programador.save()

#Consulta a tebela pessoa
def consulta_pessoas():
    programador = Programadores.query.all()
    print(programador)
    programador = Programadores.query.filter_by(nome='Julia').first()
    print(programador.idade)
if __name__ == '__main__':
    insere_programador()

    
