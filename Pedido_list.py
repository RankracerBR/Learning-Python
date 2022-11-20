import os

dados = list()

op = 1

while op > 0:
    os.system('cls')
    print('_'*40)
    print('BEM-VIND@S A LOJA JUJUMEKO')
    print('💕 OPÇÕES A BAIXO 💕')
    op = int(input('\n1 - Registrar Produto \n2 - Pedir produto \n3 - Ver produtos \n0 - Sair \n\nOpção: '))
    print('_'*40)   
    if op == 1:
        registro = input('Informe o nome do produto: ').lower()
        if registro in dados:
            print('\nEssa nome já existe')
        else: 
            dados.append(registro)
            print('\nProduto registrado com sucesso')
    if op == 2:
        pedido = input('Informe o nome do produto: ').lower()
        if pedido not in dados:
            print('Nenhum produto para retirada')
        else:
            print(f'Obrigado pelo pedido, o produto selecionado foi: {pedido}')
    if op == 3:
        if dados == []:
            print('Nenhum produto')
        if dados != []:
            print(f'Produtos registrados{dados}')
    if op == 0:
        break
    
    input('\nAperte ENTER para continuar ')