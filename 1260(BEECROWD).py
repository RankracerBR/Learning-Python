N = int(input())
linha = input()

for i in range(N):
    frequencia = dict()
    contador = 0
    while True:
        try:
            especie = input()
            if especie == '':
                break 
            else:
                contador += 1
                if especie in frequencia:
                    frequencia[especie] += 1
                else:
                    frequencia[especie] = 1
                    
        except EOFError:
            break 
    for nome in sorted(frequencia):
        percentual = frequencia[nome] / contador * 100
        print(f'{nome} {percentual:.4f}')
    if i < N-1:
        print()