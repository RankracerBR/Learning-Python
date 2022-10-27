n = int(input()) 
while n > 0:
    n -= 1
    feira = {}
    final = 0.0
    
    m = int(input())
    while m > 0:
        m -= 1
        item,valor = input().split()
        feira[item] = float(valor)
        
    p = int(input())
    while p > 0:
        p -= 1
        item, qt = input().split()
        final += feira[item] * int(qt)
        
    print(f'R${final:.2f}')    