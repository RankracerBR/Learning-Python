N = int(input())
for _ in range(N):
  inicio,fim = input().split()
  inicio = int(inicio)
  fim = int(fim)
  
  sequencia = ''
  reverso = ''
  
  for i in range(inicio,fim+1):
    sequencia += str(i)
  
  for caracter in reversed(sequencia):
    reverso += caracter
  
  print(sequencia+reverso)