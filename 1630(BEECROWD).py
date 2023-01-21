def mdc(x,y):
    while y:
        x,y = y, x % y
    return x

while True:
    try:
        x,y = map(int, input().split())
        if x == y:
            print('4')
        else:
            if x > y:
                x,y = y,x 
            divisorcomum = mdc(x, y)
            print(2*(x // divisorcomum) + 2*(y // divisorcomum))
    except EOFError:
        break