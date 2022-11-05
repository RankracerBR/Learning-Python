M,N = map(int, input().split())
monetizacao = dict()
for i in range(M):
    linha = input().split()
    monetizacao[linha[0]] = int(linha[1])
    
for i in range(N):
    salario = 0
    linha = input()
    while linha != '.':
        for palavra in linha.split():
            if palavra in monetizacao:
                salario += monetizacao[palavra]
        linha = input()
    print(salario)