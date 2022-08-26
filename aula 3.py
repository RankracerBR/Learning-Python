a = int(input('Entre com o primeiro  valor: '))
b = int(input('Entre com o segundo valor: '))
resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or not resto_b > 0:
    print('Foi digitado um número par')
else:
    print('Nenhum número par foir digirado')






#a = int(input('Primeiro valor: '))
#b = int(input('Segundo valor: '))
#c = int(input('Terceiro valor: '))
#if a > b and a > c:
 #   print('o maior número é'.format(a))
#elif b > a and b > c:
 #   print('o maior número é{}'.format(b))
#else:
#    print('o maior número é {}'.format(c))
#print('final do programa')