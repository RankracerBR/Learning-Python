
lista = [1, 10]

try: 
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    print('fechando arquivo')
except ZeroDivisionError:
    print('Não foi possível realizar divisão por 0 ')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação')
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except BaseException as ex: #BaseException é o "Pai das exceções", se só tiver ele no código ele será o primeiro a rodar
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()