while True:
    try:
        t = int(input())
        pol = input().split(' + ')
        derivada = []
        for i in pol:
            x = i.split('x')
            valor = int(x[0])* int(x[1])
            if (int(x[1]) - 1) != 1:
                derivada.append(str(valor) + 'x' + str(int(x[1]) - 1))
            else:
                derivada.append(str(valor) + 'x')
        derivada = ' + '.join(derivada)
        print(derivada)
    except EOFError:
        break