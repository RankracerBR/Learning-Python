T = int(input())

while T > 0:
    T -= 1
    r1,r2 = map(int, input().split(' '))
    total = r1 + r2
    print(total)