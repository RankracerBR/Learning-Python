n = int(input('Informe a quantidade de produtos, em seguida informe o nome dos produtos: '))
valor = 0
armazem = []

while n > 0:
    n -= 1
    produto = input()
    valor += 5
    armazem.append(produto)

print(armazem)
print(valor)
            
