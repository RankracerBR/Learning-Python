operacao = input()
matriz = []
for i in range(12):
    matriz.append([])
    for y in range(12):
        num = float(input())
        matriz[i].append(num)

contador = 0
inferior = 5 #altura de blocos verdes
superior = 7# altura dos blocos depois dos blocos verdes
soma = 0

for i in range(7,12):
    for y in range(inferior,superior):
        soma += matriz[i][y]
        contador += 1
    inferior -= 1
    superior += 1
    
media = soma / contador

if operacao == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{media:.1f}')