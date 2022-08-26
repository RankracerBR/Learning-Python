A = int(input())
B = int(input())
C = int(input())
D = int(input())

soma_cd = C + D
soma_ab = A + B

if B > C and D > A and soma_cd > soma_ab and C > 0 and D > 0 and A % 2 == 0:
  print('Valores aceitos')
else:
  print('Valores nao aceitos')