def conversor_de_dias(x):
  resultado = x // 7
  resto = x % 7
  return (f'{resultado:.0f} semana(s) e {resto:.0f} dia(s)')

teste_1 = conversor_de_dias(10)
resultado_esperado_1 = '1 semana(s) e 3 dia(s)'
print(f'resultado esperado: {resultado_esperado_1}, resultado calculado {teste_1}')

teste_2 = conversor_de_dias(25)
resultado_esperado_2 = '3 semana(s) e 4 dia(s)'
print(f'resultado esperado: {resultado_esperado_2}, resultado calculado {teste_2}')

teste_3 = conversor_de_dias(100)
resultado_esperado_3 = '14 semana(s) e 2 dia(s)'
print(f'resultado esperado: {resultado_esperado_3}, resultado calculado {teste_3}')