t = int(input())
while t:
    t -= 1
    b = int(input())
    ad, dd, ld = [int(x) for x in input().split()]
    ag, dg, lg = [int(x) for x in input().split()]
    calc1 = (ad + dd)/2.0
    calc2 = (ag + dg)/2.0
    if ld % 2 == 0:
        calc1 += b
    if lg % 2 == 0:
        calc2 += b

    if calc1 > calc2:
        print('Dabriel')
    elif calc2 > calc1:
        print('Guarte')
    else:
        print('Empate')