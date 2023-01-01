for i in range(1,10,2): #o 1 é primeiro número, já o 2 é número de soma do 1, e o número do meio é á quantidade de números i que irá aparecer
    for j in range(6+i,3+i,-1): #o j usa a mesma lógica do primeiro, portanto ele irá pegar o número 6 para somar com i, o -1 vai servir para a sequência ir diminuindo, já o do meio é a soma da sequência
        print(f'I={i} J={j}')
