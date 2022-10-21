while True:
  try:
    carnes = dict()
    n = int(input())
    for _ in range(n):
      peca, validade = input().split()
      validade = int(validade)
      carnes[peca] = validade 
    carnes_ordenadas = dict(sorted(carnes.items(), key= lambda x:x[1]))
    resultado = ' '.join(carnes_ordenadas.keys())
    #for carne in carnes_ordenadas:
     #  resultado += carne + ' '
      # print(resultado[0:-1])
  except EOFError:
    break