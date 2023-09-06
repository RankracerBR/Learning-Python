while True:
    m,n = map(int, (input()).split())
    soma = m+n
    semzero = str(soma)
    mostrar = semzero.replace('0','')
    if soma == 0:
        break
    print(mostrar)