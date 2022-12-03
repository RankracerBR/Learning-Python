def raiz10(n):
    if n == 0:
        return 6
    x = 6+1/raiz10(n-1)
    return x

n = int(input())
x = raiz10(n)-3    
print(f'{x:.10f}')