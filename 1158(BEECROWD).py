N = int(input())

total = 0

for i in range(N):
    diminuir = 0
    x,y = input().split()
    x = int(x)
    y = int(y)
    vetor = []
    if x % 2 == 0:
        x += 1
    while diminuir < y:
        vetor.append(x)
        diminuir += 1
        x += 2
    print(sum(vetor))