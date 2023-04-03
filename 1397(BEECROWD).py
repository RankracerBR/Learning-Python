n = 1
while (n != 0):
    n = int(input())
    if (n != 0):
        contador_1 = 0
        contador_2 = 0
        for i in range(n):
            a,b = map(int, input().split())
            if a > b:
                contador_1 += 1 
            elif a < b:
                contador_2 += 1
        print(contador_1,contador_2)