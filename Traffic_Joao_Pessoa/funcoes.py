import os

def exibir_menu():
    print('''
    _______________________________
    1. Adicionar Bairro
    2. Adicionar Rua
    3. Exibir Dados
    4. Exibir ruas por bairro
    5. Calcular Tráfego por bairro
    6. Calcular Tráfego total
    0. Sair
    _______________________________
    ''')
    op = int(input('Informe sua opção: '))
    return op

def adicionar_bairro(cidade):
    os.system('cls')
    bairro = input('Informe o bairro: ')
    if bairro not in cidade:
        cidade[bairro] = {}
    else:
        print('O bairro já está cadastrado')

def exibir_dados(cidade):
    for bairro, ruas in cidade.items():
        print(f'{bairro}: ')
        for nome, trafego in ruas.items():
            print(f'\t {nome} - {trafego} carros/hora')

def adicionar_rua(cidade):
    os.system('cls')
    bairro = input('Informe o bairro: ')
    if bairro in cidade:
        rua = input('Informe a rua/avenida: ')
        if rua not in cidade[bairro]:
            trafego = int(input('Informe o tráfego da rua: '))
            cidade[bairro][rua] = trafego
        else:
            print('Rua/Avenida já cadastrada')
    else:
        print('Bairro ainda não cadastrado')

def exibir_rua_bairro(cidade):
    os.system('cls')
    bairro = input('Informe o bairro')
    if bairro in cidade:
        ruas = cidade[bairro]
        for rua, trafego in ruas.items():
            print(f'{rua} - {trafego} carros/hora')
    else:
        print('Bairro não cadastrado')

def calculo_trafego_bairro(cidade):
    contador = 0
    bairro = input('Informe o nome do bairro: ')
    if bairro in cidade:
        ruas = cidade[bairro]
        for rua, trafego in ruas.items():
            contador += trafego
        print(contador)
    else:
        print('Bairro não cadastrado')

def trafego_total(cidade):
    os.system('cls')
    contador_total = 0
    for bairro, ruas in cidade.items():
        for rua, trafego in ruas.items():
            contador_total += trafego
        print(f'>Número total do tráfego no Bairro: {bairro}')
        print(f'{contador_total}')