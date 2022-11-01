nota = {'W':1, 'H':1/2, 'Q':1/4, 'E':1/8, 'S':1/16, 'T':1/32, 'X':1/64}

while True:
    compasso = input()
    if compasso == '*':
        break
    compasso = [x for x in compasso.split('/') if x]
    total = 0
    
    for conjunto in compasso:
        d = 0
        for i in conjunto:
            d += nota[i]
            if d > 1:
                break
        if d == 1:
            total += 1
            
    print(total)