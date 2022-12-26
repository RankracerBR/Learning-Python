P1, C1, P2, C2 = map(int, input().split())

resultado1 = P1 * C1
resultado2 = P2 * C2

if resultado1 == resultado2:
  print(0)
elif resultado1 > resultado2:
  print(-1)
else:
  print(1)