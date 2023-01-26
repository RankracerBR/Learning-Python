hora1,min1,hora2,min2 = list(map(int, input().split()))

calculo = ((hora2*60) +min2)-((hora1 * 60)+ min1)

if (calculo <=0):
    calculo += 24*60

horario = calculo // 60
minuto = calculo % 60

print(f'O JOGO DUROU {horario} HORA(S) E {minuto} MINUTO(S)')