while True:
    try:
        v, t = map(int, input().split())
        multi = v * t * 2
        print(multi)
    except EOFError:
        break
