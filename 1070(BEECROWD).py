numero = int(input())

impares = [n for n in range(numero,numero+12)if n % 2 != 0]
for n in impares:
    print(n)