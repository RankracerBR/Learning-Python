l1  = input().split(' ')
l2 = input().split(' ')

cd1,qt1,valor1 = l1 
cd2,qt2,valor2 = l2

total = (int(qt1) * float(valor1)) + (int(qt2) * float(valor2))

print(f'VALOR A PAGAR R${total:.2f}')