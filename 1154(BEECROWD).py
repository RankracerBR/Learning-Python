x = 0
y = 0
while True:
    try:
        n = int(input())
        if n < 0:
            break 
        else:
            x = x + n
            y = y + 1
    except EOFError:
        break
c = x/y
print(f'{c:.2f}')