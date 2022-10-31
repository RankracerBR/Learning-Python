n = int(input())

for i in range(n):
 t = input()
 rgb = list(map(int,input().split()))

 if t == 'eye':
  x = int(0.3*rgb[0] + 0.59*rgb[1] + 0.11*rgb[2])
 elif t == 'mean':
  x = sum(rgb)//3
 elif t == 'max':
  x = max(rgb)
 else:
  x = min(rgb)

 print("Caso #{}: {}".format(i+1, x))