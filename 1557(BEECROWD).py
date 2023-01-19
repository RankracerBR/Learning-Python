n = 1

while n != 0:
    n = int(input())
    if n == 0:
        break 
    m = list()
    
    #Matriz    
    for i in range(n):
        m.append([])
        for j in range(n):
            m[i].append(0)
    
    #Elementos        
    m[0][0] = 1
    for i in range(0,n):
        if i >=1:
            m[i][0] = m[i - 1][0] * 2
            
        for j in range(1, n):
            m[i][j] = m[i][j-1] * 2
    
    #print
    
    t = len(str(m[n-1][n-1]))
    for i in range(n):
        for j in range(n):
            m[i][j] = str(m[i][j])
            while len(m[i][j]) < t: 
                m[i][j] = ' ' + m[i][j]
                
        M = ' '.join(m[i])
        print(M)
    print()