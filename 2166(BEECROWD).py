def raiz2(n):
    if n == 0:
        return 2
    calculo = 2+1/raiz2(n-1)
    return calculo

n = int(input())
calculo = raiz2(n)-1
print(f'{calculo:.10f}')

