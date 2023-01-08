import math 
n = int(input())
minimo = n / math.log(n)
maximo = (1.25506 * n) / math.log(n)
print(f'{minimo:.1f} {maximo:.1f}')