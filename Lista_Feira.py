from cgi import print_form


lista = dict()
resp = 'sim'

while resp == 'sim':
    produto = input('Informe o produto: ')
    preco = float(input('Informe o preço do produto: '))
    quantidade = float(input('Informe a quantidade: '))
    lista[produto] = {'preço': preco, 'quantidade': quantidade}
    resp = input('Deseja continuar (sim/não): ')
    
lista_ordenada_pelo_preco = dict(sorted(lista.items(), key= lambda x:x[1]['preço']))

total = 0 

for chave in lista_ordenada_pelo_preco:
    total += lista[chave]['preço'] * lista[chave]['quantidade']
    print(chave, lista[chave]['preço'], lista[chave]['quantidade'])

print(f'Total da lista R$ {total}')