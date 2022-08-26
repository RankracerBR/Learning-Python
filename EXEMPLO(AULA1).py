idade = int(input('Informe a sua idade: '))
renda = float(input('Informe a sua renda: '))

if idade >= 18 and renda >= 2000.00: 
   print('Você é maior de idade\n')
   print('Você pode tirar a CNH')
elif idade == 17:
  print('Você  pode se matricular na auto escola')  
else:  
  print('Você não pode tirar a carteira de motorista')