# Contar a quantidade de passos percorridos em números pares e impares
n = int(input())
passos = 0 

if n > 0:
  while n > 1:
    if n % 2 == 0:
      n = n /2 
    else:
      n = 3*n + 1
      passos += 1
  print(passos)
else:
  print('impossível calcular')

    
