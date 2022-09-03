import os

def listar_filmes(lista):
  print(f'Existem {len(lista)} filmes cadastrados\n\n');
  print('Título'.ljust(30,' '), 'Diretor'.ljust(30,' '),'Ano'.ljust(30,' '),'Disponibilidade'.ljust(30,' '))
  print('-'*120)
  for filme in lista:
    for info in filme[0:-1]:
      print(info.ljust(30,' '),end='|')
    if filme[-1] == True:
      print('Disponível'.ljust(30,' '))
    else:
      print('Alugado'.ljust(30,' '))


filme_1 = ['The Batman', 'Matt Reeves', '2022', True]
filme_2 = ['Doutor Estranho 2', 'Sam Raimi','2022',True]
filme_3 = ['Seven, os sete pecados', 'David Fincher', '1997', False]

acervo = [filme_1, filme_2, filme_3]

tamanho = os.get_terminal_size()
largura = tamanho[0]

op = 1
while op != 0:
  os.system('clear')
  print('-'*largura)
  print('PyBuster'.center(largura))
  print('-'*largura)
  print('Menu de opções: ')
  print('1 - Listar Filmes\n2 - Cadastrar Filmes\n3 - Pesquisar\n0 - SAIR')
  op = int(input('\nInforme a sua opção: '))

  if op == 1:
    os.system('clear')
    listar_filmes(acervo)
    
    input('\n\ndigite ENTER para continuar: ')
  elif op == 2:
    os.system('clear')
    resp = 'sim'
    while resp == 'sim':
      titulo = input('Informe o título do filme: ')
      diretor = input('Informe o diretor do filme: ')
      ano = input('Informe o ano do filme: ')
      filme = [titulo,diretor,ano,True]
      acervo.append(filme)
      resp = input('Deseja cadastrar outro filme: ').lower()
  elif op == 3:
    os.system('clear')
    palavra = input('Informe a palavra para pesquisar: ')
    palavra = palavra.lower()
    resultados = []
    for filme in acervo:
      if palavra in filme[0].lower():
        resultados.append(filme)    
    
    listar_filmes(resultados)
    input('aperte ENTER para continuar')
  elif op == 0:
    print('Até mais humano!')
  else:
    os.system('clear')
    print('Opção inválida')
    input('aperte ENTER para continuar')