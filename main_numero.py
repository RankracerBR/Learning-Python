from funcoes_numero import eh_numero_armstrong
numeros = int(input('Digite um valor: '))
valor = eh_numero_armstrong(numeros)

if valor == True:
  print('É número Armstrong')
if valor == False:
  print('Número não Armstrong')

print(valor)