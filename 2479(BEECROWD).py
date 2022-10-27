n = int(input())

lista = []
bom = 0

while n > 0:
    n -= 1
    c, nome = input().split()
    lista.append(nome)
    if c == '+':
        bom += 1
        
lista.sort()

for x in lista:
    print(x)

print(f'Se comportaram: {bom} | Nao se comportaram: {len(lista)-bom}')