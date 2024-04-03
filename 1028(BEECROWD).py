casos = int(input())

while casos > 0:
    ricardo, vicente = map(int, input().split())
    while vicente != 0:
        resultado = ricardo % vicente
        ricardo = vicente
        vicente = resultado
    print(ricardo)
    casos -= 1