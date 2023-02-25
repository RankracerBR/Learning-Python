a = [1,2,3]
b = [4,5,6]

acumulador = 0

for valor_1, valor_2 in zip(a,b):
    acumulador += valor_1 + valor_2 
print(acumulador)