vezes_1 = 0
vezes_2 = 0
vezes_3 = 0

op = 1

while op != 0:
    combustivel = int(input())
    if combustivel == 1:
       vezes_1 = vezes_1 + 1
       print(f'Alcool: {vezes_1}')
    elif combustivel == 2:
            vezes_2 = vezes_2 + 1
            print(f'Gasolina: {vezes_2}')  
    elif combustivel == 3:
            vezes_3 = vezes_3 + 1
            print(f'Diesel: {vezes_3}')
    elif combustivel == 4: 
        print()
        break     