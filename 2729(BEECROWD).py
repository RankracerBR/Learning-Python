N = int(input())

for x in range(N):
    lista = set(input().split())
    lista_ordenada = sorted(lista)
    resultado = ' '.join(lista_ordenada)
    print(resultado)