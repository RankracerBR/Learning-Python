while True:
    try:
        n = int(input())
        l = input().split()
        cont = 0

        for i in range(n):
           if int(l[i]) > cont: 
            cont = int(l[i])

        if cont < 10:
            N = 1
        elif cont >= 10 and cont < 20:
            N = 2
        else:
            N = 3
        print(N)

    except EOFError:
        break