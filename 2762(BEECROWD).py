while True:
    try:
        n = [int(x) for x in input().split('.')]
        n = n[::-1]
        n = '.'.join(str(x) for x in n)
        print(n)
    except EOFError:
        break
