M=[]
O = input()

for i in range(12):
    M.append([])
    for j in range(12):
        y = float(input())
        M[i].append(y)

soma = 0
contador = 0
col = 11
for i in range(1,11):
    for j in range(col,12):
        soma += M[i][j]
        
        contador += 1
    if i < 5:
        col -= 1
    if i > 5:
        col += 1
    
    

media = soma / contador

if O == "S":
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(media))