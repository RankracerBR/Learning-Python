T = int(input())

for i in range(T):
    T -= 1
    n = int(input())
    soma = (1 << n) - 1
    print(soma)