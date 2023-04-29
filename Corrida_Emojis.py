import time
import random
import os


emojis = {"🚀": 0, "🚗": 0, "🏎": 0, "🛵": 0, "🚲": 0,"🥳":0,"👾":0,"😎":0}
print('_'*80)
print(emojis)
print('_'*80)
print('\n')

while True:
  
  pergunta = int(input('Quanto passos o emoji ganhador irá dar:'))
  for passo in range(1, 10):
    os.system("clear")
    for emoji, posicao in emojis.items():
      distancia = random.randint(1, 4)
      emojis[emoji] += distancia
      print(f"{emoji} {f'{emoji}' * emojis[emoji]}{emoji}")
    time.sleep(2)
  
  os.system("clear")
  print(f'>Passos do emoji ganhador: {posicao}')
  emoji_ganhador = max(emojis, key=emojis.get)
  emoji_perdedor = min(emojis, key=emojis.get)
  print(f'>O vencedor é: {emoji_ganhador}')
  print(f'>O perdedor é: {emoji_perdedor}')
  
  if pergunta != posicao:
     print('(X) Que pena, você errou 😞')
  if pergunta == posicao:
    print('(V)PARABÉNS, VOCÊ GANHOU UM PRÊMIO 😀')