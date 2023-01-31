N,S = map(int, input().split())
menor = 1001

while N:
    N -= 1
    S += int(input())
    if S < menor:
        menor = S 

print(menor)