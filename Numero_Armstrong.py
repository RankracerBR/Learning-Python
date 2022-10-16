from Funcao_Numero_Armstrong import eh_numero_armstrong
numero = int(input('Digite um valor: '))
valor = eh_numero_armstrong(numero)

if valor == True:
    print('É número Armstrong')
if valor == False: 
    print('Número não Armstrong')