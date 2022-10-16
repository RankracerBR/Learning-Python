contador = dict() #ao invés de usar o dict pode usar {} que o python já vai identificar como um dicionário

frase = input('Informe uma frase: ')

for letra in frase: 
    letra = letra.lower()
    if letra not in contador:  #se não aparecer a mesma letra outra vez, o 'not in' iguala a um
        contador[letra] = 1 
    else: 
        contador[letra] += 1
for c in sorted(contador): #'sorted' é o comando que organiza em ordem alfabética as letras
    print(f'{c} - {contador[c]}')