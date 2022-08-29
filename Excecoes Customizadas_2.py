
class Error(Exception):
    pass#o pass não faz absolutamente nada, mas sever para não deixar o código vazio

class InputError(Error):
    def __init__(self, message):   
       self.message = message



while True: #while True sempre irá executar se for verdadeiro
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10') #o raise força uma exceção 
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break #Se a resposta for um número, a execução irá parar, caso não, sempre irá ser executado o input
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas númeors.')
    except InputError as ex:
        print(ex)
