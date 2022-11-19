import getpass #esconde a senha 

class Conta:
    def __init__(self,nome,senha,n_conta,saldo=0):#cuidado para não alterar a sequência
        self.nome = nome
        self.n_conta = n_conta
        self.saldo = saldo
        self.senha = senha 
        self.operacoes = []
    def __str__(self):
        return f'Cliente: {self.nome} - N* Conta: {self.n_conta} - Saldo: {self.saldo}'
    
    def deposito(self,dinheiro):
        if dinheiro > 0:
            self.saldo = self.saldo + dinheiro 
            print(f'Depósito de R$ {dinheiro} efetuado com sucesso')
            self.operacoes.append(f'DEPÓSITO - R${dinheiro}')
        else:
            print('Valor inválido para depósito')
    
    def saque(self):
        senha = getpass.getpass('Informe a senha: ')
        if senha != self.senha:
            print('Senha incorreta!!')
        else:
            valor = float(input('Informe o valor para o saque: '))
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor 
                print('Saque efetuado com sucesso')
                self.operacoes.append(f'SAQUE - R$ {valor}')
            else:
                print('Valor inválido para o saque')
        
    def extrato(self):
        senha = getpass.getpass('Informe a senha: ')
        if senha != self.senha:
            print('Senha incorreta')
        else:
            for operacao in self.operacoes:
                print(operacao)
            print(f'Saldo atual R$ {self.saldo:.2f}')