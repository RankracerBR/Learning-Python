filme_1 = ['The Batman', 'Matt Reeves', '2022', True]
filme_2 = ['Doutor Estranho 2', 'Sam Raimi','2022',True]
filme_3 = ['Seven, os sete pecados', 'David Fincher', '1997', False]

acervo = [filme_1, filme_2, filme_3]

resp = 'sim'

while resp == 'sim' or resp == 'Sim':
  titulo = input('Informe o titulo do fime: ')
  diretor = input('Informe o diretor do filme: ')
  ano = input('Informe o ano do filme: ')
  filme = [titulo,diretor,ano,True]
  acervo.append(filme)
  resp = input('Deseja cadastrar outro filme: ').lower()

print(f'Existem {len(acervo)} filmes cadastrados\n\n');
print('Título'.ljust(30,' '), 'Diretor'.ljust(30,' '),'Ano'.ljust(30,' '),'Disponibilidade'.ljust(30,' '))
print('-'*120)
for filme in acervo:
  for info in filme[0:-1]:
    print(info.ljust(30,' '),end='|')
  if filme[-1] == True:
    print('Disponível'.ljust(30,' '))
  else:
    print('Alugado'.ljust(30,' '))