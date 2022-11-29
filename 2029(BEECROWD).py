while True:
    try:
        V = float(input())
        D = float(input())
        r = D/2
        area = 3.14*r*r
        altura = V/(r*r*3.14)
        print(f'ALTURA = {altura:.2f}')
        print(f'AREA = {area:.2f}')
    except EOFError:
        break