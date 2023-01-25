n = int(input())
c = [int(x) for x in input().split()]

while len(c) != 1:
   t = []
   for i in range(len(c)-1):
      if c[i] == c[i+1]: t.append(1)
      else: t.append(-1)
   c = t[:]
if t[0] == -1: print('branca')
else: print('preta')