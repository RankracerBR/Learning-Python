import random
import time
import os

emojis = {"🚀":0, "🚗":0, "🏎":0, "🛵":0, "🚲":0}
passos = 10

for passo in range(1, passos):
    os.system("cls")
    for emoji, posicao in emojis.items():
        distancia = random.randint(1,4)
        emojis[emoji] += distancia
        print(f"{emoji} {' ' * emojis[emoji]}{emoji}")
    time.sleep(1)

winning_emoji = max(emojis, key=emojis.get)
print(f'O vencedor é: {winning_emoji}')