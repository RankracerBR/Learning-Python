while True:
    try:
        n,m = [int(x) for x in input().strip().split(' ')]
        if (n == 0 and m == 0):
            break 

        b = [int(x) for x in input().strip().split(' ')]
        
        r = 0
        c = [0  for i in range(n+1)]

        for bilhete in b:
            c[bilhete] += 1
            if (c[bilhete] == 2):
                r += 1        
        print(r)

    except EOFError:
        break