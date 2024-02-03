while True:
    try:
        direcao = input()

        if direcao == 'esquerda':
            print('ingles')
        elif direcao == 'direita':
            print('frances')
        elif direcao == 'nenhuma':
            print('portugues')
        elif direcao == 'as duas':
            print('caiu')
    except EOFError:
        break
