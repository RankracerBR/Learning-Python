def soma_pares(n):
    if n <= 1:
        return None 
    i = 1 
    soma = 0
    while i <= n:
        i += 1
        if i % 2 == 0:
            soma += i
    return soma 

print(soma_pares(10))  