while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        cvz,ano,tempo = input().split()
        ano = int(ano)
        tempo = int(tempo)
        if i == 0:
            menor = ano - tempo
            ganha= cvz
        if menor > ano - tempo:
            menor = ano - tempo 
            ganha = cvz
    print(ganha)