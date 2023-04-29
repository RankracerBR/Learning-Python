while  True:
    n = int(input())

    if n == 0:
        break

    resultado =  []

    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(1)
        resultado.append(tmp)

    valor = 1
    cima = 0
    esq = 0
    baixo = n - 1
    direita = n - 1

    if n % 2 == 0:
        meio = n / 2

    else:
        meio = n + 1 / 2


    while valor <= meio:
        i = esq
        while i <= direita:
            resultado[cima][i] = valor
            resultado[baixo][i] = valor
            i+=1

        i = cima + 1
        while  i < baixo:
            resultado[i][esq] = valor
            resultado[i][direita] = valor
            i+=1

        valor+=1
        cima+=1
        baixo-=1
        esq+=1
        direita-=1

    for i in range(n):
        txt = ''
        for j in range(n):
            txt += " %3d" %resultado[i][j]
        print(txt[1:])
    print("")