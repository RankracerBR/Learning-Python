preco = 24.95
desconto = 40 / 100
frete_1 = 3.00
frete_atacado = 0.75
quantidade = 60
preco_desconto = preco - desconto*preco     
total = quantidade * preco_desconto + frete_1 + (quantidade -1)*frete_atacado
print(f'{preco_desconto:.2f}')
print(f'O preço final é de R$ {total:.2f}')