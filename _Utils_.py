from Banco_de_dados_SQLAlchemy import Pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='Julia',idade=19)
    print(pessoa)
    pessoa.save()
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Julia').first()
    print(pessoa.idade)
def altera_pessoa():
    pessoa =  Pessoas.query.filter_by(nome='Julia').first()  
    pessoa.nome = 'Felipe'
    pessoa.save()
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()
if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
   