q = int(input())

for i in range(q):
    t = input()
    
    c =0
    a = 0
    a1 = 0
    ka = 'k' 
    
    for x in range(len(t)):
        if t[x] == 'k':
            a = c 
            c= 0
        elif t[x] == 'a':
            c += 1
    a1 = c
    
    a2 = a1 * a
    
    for x in range(2):
        ka += 'a'
    print(ka)