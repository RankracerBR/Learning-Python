while True:
    try:
        N = int(input())
        matriz = []
        for i in range(0,N):
            matriz.append([])
            for j in range(0,N):
                matriz[i].append('3')
            c1 = N - 1
        for i in range(0,N):    
            matriz[i][i] = '1'
            matriz[i][c1] = '2'
            c1 -= 1
            M = ''.join(matriz[i])
            print(M)
    except EOFError:
        break