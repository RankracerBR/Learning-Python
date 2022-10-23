import random 

for x in range(10): #intervalo
    numeros = set() #o set armazena os valores
    while len(numeros) < 6: #quantos números devem aparecer
        n = random.randint(1,60)#radint gera aleatoriamente um número 
        numeros.add(n)
    print(sorted(numeros))#sorted deixa os números em ordem crescente