while True:
    try:
        n = int(input())
        tamanho = int(n/3)
        o = (n-tamanho)

        #Parte Extena (0)
        m =[[0 for i in range(n)] for j in range(n)]
        
        #Diagonal Principal (2)
        for i in range(n):
            m[i][i] = 2
            
        #Diagonal Secundária (3)
        j = 0
        for i in range(n-1,-1,-1):
            m[j][i] = 3
            j+=1
            
        #Parte Interna (1)
        for i in range(tamanho,o):
            for j in range(tamanho,o):
                m[i][j] = 1
        
        m[int(n/2)][int(n/2)] = 4
        
        for i in range(n):
            for j in range(n):
                print(m[j][i], end="")
            print()
        print()
    except EOFError:
       break 