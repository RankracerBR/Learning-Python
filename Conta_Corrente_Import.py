from Conta_Corrente_class import Conta       
import getpass  
import os 

banco = dict() #as informações serão armazenadas aqui só quando o programa rodar

op = '1'
while op != '0':
    os.system('cls')
    print('_'*40)
    op = input('1 - Cadastrar\n2 - Listar Contas\n3 - Depósito\n4 - Saque\n5 - Extrato\n0 - Sair\nOpção: ')
    print('_'*40)
    if op == '1': #Cadastrar
        nome = input('Informe o nome do cliente: ')
        n_conta = input('Informe o número da conta: ')
        senha = getpass.getpass('Informe a senha: ')
        if n_conta in banco:
            print('Essa conta já existe')
        else: 
            conta = Conta(nome,senha,n_conta)
            banco[n_conta] = conta 
            print('Conta cadastrada com sucesso\n')
        input('\n\nDigite ENTER para voltar')
    elif op == '2': #Listar
        for numero in banco:
            print(banco[numero])
        input('\n\nDigite ENTER para voltar')
    elif op == '3':
        n_conta = input('Informe a conta para o depósito: ')
        if n_conta in banco:
            valor = float(input('Informe o valor para deposito: '))
            banco[n_conta].deposito(valor)
        else:
            print('Essa conta não existe')
        input('\n\nDigite ENTER para voltar')
        
    elif op == '4':
        n_conta = input('Informa a conta para o saque: ')
        if n_conta in banco:
            banco[n_conta].saque()
        else:
            print('Conta inexistente')
        input('\n\nDigite ENTER para sair')
    elif op == '5':
        n_conta = input('Informa a conta para o extrato: ')
        if n_conta in banco:
            banco[n_conta].extrato()
        else:
            print('Conta inexistente')
        input('\n\nDigite ENTER para sair')