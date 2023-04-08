h1,h2 = map(int, input().split())
if h1 < h2:
    tempo = h2 - h1
else:
    tempo = h2+24 - h1
print(f'O JOGO DUROU {tempo} HORA(S)')