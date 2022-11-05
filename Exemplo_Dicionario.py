frequencia = dict()

while True:
    try:
        nome = input()
        if nome in frequencia:
            frequencia[nome] += 1
        else:
            frequencia[nome] = 1
    except EOFError:
        break
print(f'Quantidade de nomes diferentes: {len(frequencia)}')
for nome in sorted(frequencia):
    percentual = frequencia[nome] / len(frequencia) * 100
    print(f'{nome} - {percentual:>3f}')