def fatorial(n):
    if n < 0:
        return None 
    produto = 1
    i = 1 
    while i <= n:
        produto = produto * i 
        i += 1 
    return produto 

numero = 5
resultado = fatorial(numero)
print(f'O fatorial de {numero}! = {resultado}')