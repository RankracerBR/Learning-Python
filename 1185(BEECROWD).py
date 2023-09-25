matriz = []

opcao = input()

desincrementar = 12
soma = 0
contador = 0

for i in range(12):
    matriz.append([])
    for j in range(12):
        x = float(input())
        matriz[i].append(x)

for i in range(11):
    desincrementar -= 1
    for j in range(desincrementar):
        soma += matriz[i][j]
        contador += 1

if opcao == 'S':
    print(f'{soma:.1f}')

if opcao == 'M':
    mediana = soma / contador
    print(f'{mediana:.1f}')