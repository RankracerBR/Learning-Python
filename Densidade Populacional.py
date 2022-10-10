def densidade_populacional(x,y):
  populacao = x
  area = y
  resultado = populacao/area
  return resultado


teste_1 = densidade_populacional(10,1)
resultado_esperado_1 = 10
print(f'resultado esperado: {resultado_esperado_1:.2f}, resultado calculado {teste_1:.2f}')

teste_2 = densidade_populacional(864816, 121.4)
resultado_esperado_2 = 7123.6902801
print(f'resultado esperado: {resultado_esperado_2:.7f}, resultado calculado {teste_2:.7f}')