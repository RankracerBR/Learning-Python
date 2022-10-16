from Funcao_Ano_Bissexto  import ano_bissexto

ano_ = int(input('Informe um ano: '))
ano_bi = ano_bissexto(ano_)
if ano_bi == True:
    print('Ano Bissexto')
if ano_bi == False: 
    print('Ano não Bissexto')