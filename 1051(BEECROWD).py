total = float(input())

if total <= 2000:
  print('Isento')
elif total <= 3000:
  total = total - 2000
  imposto = total * 0.08
  print(f'R$ {imposto:.2f}')
elif total <= 4500:
  total = total - 3000
  imposto = 1000 * 0.08
  imposto += total * 0.18
  print(f'R$ {imposto:.2f}')
else:
  total = total - 4500
  imposto = 1000 * 0.08
  imposto += 1500 * 0.18
  imposto += total * 0.28
  print(f'R$ {imposto:.2f}') #.2f representa a quantidade de número que irão se rmostrados no comando print