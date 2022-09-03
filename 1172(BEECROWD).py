X = []

for i in range(10):
  valor = int(input())
  X.append(valor)

for i in range(10):
  if X[i] <= 0:
    X[i] = 1

for i in range(10):
  print(f'X[{i}] = {X[i]}')
  