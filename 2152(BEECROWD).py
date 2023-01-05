for u in range(int(input())):
    h,m,b =  input().split()
    h = int(h)
    m = int(m)
    b = int(b)
    if b == 1:
        print(f'{h:02}:{m:02} - A porta abriu!')
    else:
        print(f'{h:02}:{m:02} - A porta fechou!')