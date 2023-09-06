caso = 1
while True:
    try:
        sequencia1 = input()
        sequencia2 = input()
        print(f'Caso #%d:' % caso)
        quantidade = sequencia2.count(sequencia1)
        if quantidade == 0:
            print('Nao existe subsequencia')
        else:
            print(f'Qtd.Subsequencias: %d' % quantidade)
            quantidade = sequencia2.rfind(sequencia1)
            print(f'Pos: %d' % (int(quantidade)+1))
        print()
        caso += 1
    except EOFError:
        break