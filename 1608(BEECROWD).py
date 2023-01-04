for q in range(int(input())):
    d,i,b = [int(x) for x in input().split()]
    ind= [int(x) for x in input().split()]
    bolos = [0 for x in range(b)]
    for l in range(b):
        o = [int(x) for x in input().split()][1:]
        bolos[l] = 0
        for y in range(0, len(o), 2):
            bolos[l] += ind[o[y]] * o[y+1]
    print(d // min(bolos))