from Orientacao_Objeto_Aluno import Aluno 

fulano = Aluno('Fulano',2022143001,[100,40,50])
beltrano = Aluno('Beltrano', 2022143002, [35,60,80])

print(f'A média de {fulano.nome} é {fulano.media():.2f}')
print(f'A média de {beltrano.nome} é {beltrano.media():.2f}')