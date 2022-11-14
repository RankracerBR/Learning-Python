n = int(input())

if 1 <= n <= 50:
    mina = list(range(n))
    for x in range(n):
        mina[x] = 0
    for x in range(n):
        v = int(input())
        if v == 1:
            mina[x] += 1
            if x == 0:
                mina[x+1]+=1
            elif x == (n-1):
                mina[x-1]+=1
            else:
                mina[x+1]+=1
                mina[x-1]+=1
    
    for y in range(n):
        print(mina[y])