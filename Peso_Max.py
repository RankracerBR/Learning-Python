pesos = [2,3,5]
quantidade = [0,0,0]
volumes = [5,4,3]
fora_estoque = [0,0,0]
PESO_MAX = 25
peso_total = 0
lista_produtos = input().upper().split()

for produto in lista_produtos:
    if produto == 'X' and pesos[0] + peso_total <= PESO_MAX and quantidade[0] < volumes[0]:
        peso_total += pesos[0]
        quantidade[0] += 1
    elif  produto == 'Y' and pesos[1] + peso_total <= PESO_MAX and quantidade[1] < volumes[1]:
        peso_total += pesos[1]
        quantidade[1] += 1
    elif  produto == 'Z' and pesos[2] + peso_total <= PESO_MAX and quantidade[2] < volumes[2]:
        peso_total += pesos[1]
        quantidade[2] += 1
    else:
        if produto == 'X':
            fora_estoque[0] += 1
        elif produto == 'Y':
            fora_estoque[1] += 1
        elif produto == 'Z':
            fora_estoque[2] += 1

print(f'Peso Total = {peso_total} kg')
print(f'Produtos no estoque = {quantidade}')
print(f'Produtos fora do estoque = {fora_estoque}')

print('Lista Original = ', end=' ')
for produto in lista_produtos:
    print(produto, end=' ')