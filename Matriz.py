matriz = []

for x in range(3):
    linha = []
    for y in range(3):
        n = int(input(f'Elemento [{x}][{y}]: '))
        linha.append(n)
        matriz.append(linha)
    
for lista in matriz:
    for n in lista:
        print(n, end=' ')
    print()