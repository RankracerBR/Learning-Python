while True:
    d, n = input().split()
    d = int(d)

    if d == 0 or n == '0':
        break

    n = n.replace(str(d), '')

    if n == '':
        print(0)
    else:
        print(int(n))