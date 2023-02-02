n = int(input())

menor_valor = 10000000.0

for i in range(1, n+1):
    a = [float(x) for x in input().split()]
    p,g = a[0], a[1]
    valor = (p * 1000) / g
    if valor < menor_valor:
        menor_valor = valor

print(f'{menor_valor:.2f}')