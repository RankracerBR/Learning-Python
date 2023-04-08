while True:
    try:
        q = int(input())
        total = []
        for i in range(q):
            q -= 1
            total.append(input().split())
            total[-1][2] = int(total[-1][2])
        total.sort(key= lambda x: (x[2],x[1],x[0]))
        for nome in total:
            print(nome[0])
    except EOFError:
        break
   