import random
import string

def opcoes(tamanho_senha,tipo_senha):
    if tamanho_senha < 4 or tamanho_senha > 20:
        print('Tamanho inválido')
    if tipo_senha == 'Letra':
        caracter = string.ascii_letters
        senha_gerada = ''.join(random.choice(caracter) for _ in range(tamanho_senha))
        print(senha_gerada)
    elif tipo_senha == 'Numero':
        caracter = string.digits
        senha_gerada = ''.join(random.choice(caracter) for _ in range(tamanho_senha))
        print(senha_gerada)
    elif tipo_senha == 'Simbolos':
        caracter = string.punctuation
        senha_gerada = ''.join(random.choice(caracter) for _ in range(tamanho_senha))
        print(senha_gerada)
    else:
        print('Formato Inválido')


senha = int(input('Digite o tamanho da senha: '))
tipo_senha = input('Digite o tipo da senha(Letra, Numero, Simbolos):')

opcoes(senha,tipo_senha)


    