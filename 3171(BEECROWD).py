def se_completo(n,l,conexoes):#obtenção dos dados
    grafic = [[] for y in range(n)]
    for x,y in conexoes:
        grafic[x-1].append(y-1)
        grafic[y-1].append(x-1)
    vi = [False] * n
    queue = []
    queue.append(0)
    vi[0] = [True]
    while queue:
        m = queue.pop(0)
        for i in grafic[m]:
            if not vi[i]:
                queue.append(i)
                vi[i] = True
    return "COMPLETO" if all(vi) else "INCOMPLETO"
#input da quantidade peças do LED
n,l = map(int, input().split()) 
conexoes = [tuple(map(int, input().split()))for y in range(l)] #cada parte do LED 
print(se_completo(n,l,conexoes))
