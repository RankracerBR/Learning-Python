n = 1
while n > 0:
    n = int(input())
    if n == 0: 
        break 
    soma = 0
    for i in range(1,n+1): 
        soma += i * i
    print(soma)