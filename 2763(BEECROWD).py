while True:
    try:
        n = input()
        n = n.replace('-','.')
        n = n.split('.')
        for i in n:
            print(i)
    except EOFError:
        break