N = int(input())

for i in range(N):
    x,y = map(int, input().split())
    if y == 0:
        print('divisao impossivel')
    if y !=0:
        div = x / y
        print(div)