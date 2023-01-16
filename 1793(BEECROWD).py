n = int(input())
while n != 0:
    tempo = list(map(int, input().split()))
    inicio = tempo[0]
    fim = tempo[0] + 10
    tempo_total = 0
    for i in range(1, n):
        if tempo[i] <= fim:
            fim = max(fim, tempo[i] + 10)
        else:
            tempo_total += fim - inicio
            inicio = tempo[i]
            fim = tempo[i] + 10
    tempo_total += fim - inicio
    print(tempo_total)
    n = int(input())