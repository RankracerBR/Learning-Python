# Contar a quantidade de passos percorridos em números pares e impares
n = int(input())
passos = 0
while 1 <= n:
    if n % 2 ==0:
        n = n - 2
        n / 2
        passos = passos + 1
        print(f'{passos}. {n}')
    if n % 1 == 0:
        n = n - 1
        (n * 3) + 1
        passos = passos + 1
        print(f'{passos}. {n}')

    
