palavras_definidas = ['Carro','Gatos','Pneus','Poste']

palpite = input('Dê o seu palpite e coloque uma palavra com menos de 5 caracteres: ')

if len(palpite) > 5:
    print('Você não pode digitar mais de 5 caracteres') 
else:
    if palpite in palavras_definidas:
        print(f'Palavras definidas: {palavras_definidas}')
        print(f'Seu palpite: {palpite}')
        print('Parabéns :3 !')
    elif len(palpite) < 5:
        print(f'Palavra não listada: {palpite}')