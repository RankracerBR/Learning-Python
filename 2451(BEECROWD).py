def atualizar_pontos(letra,pontos,maximo): #
    if letra == 'o':
        pontos += 1
        maximo = max(pontos,maximo) #pega os valores máximos
    elif letra == 'A':
        maximo = max(pontos,maximo)
        pontos = 0
    return pontos,maximo 

n = int(input()) 
tabuleiro = []
for x in range(n): #quantas linhas tem no N
    linha = input() #digita as infos
    tabuleiro.append(linha) #coloca na lista
    
pontos = 0
maximo = 0

for x in range(n):
    if x % 2 == 0: #se o número de linhas for par
        for y in range(n):
            pontos,maximo = atualizar_pontos(tabuleiro[x][y],pontos,maximo)
    else: #se as linahs forem ímpares
        for y in reversed(range(n)): #vê as infos ao contrário
            pontos,maximo = atualizar_pontos(tabuleiro[x][y],pontos,maximo)
print(maximo)