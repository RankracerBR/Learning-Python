N = int(input())

multiplo2 = 0
multiplo3 = 0
multiplo4 = 0
multiplo5 = 0

valores = input().split(' ')
valores_corretos = valores[:N] #!!!!

for i in range(N):
    valores_corretos[i] = int(valores_corretos[i])    
    if valores_corretos[i] % 2 == 0:
        multiplo2 += 1
    if valores_corretos[i] % 3 == 0:
        multiplo3 += 1
    if valores_corretos[i] % 4 == 0:
        multiplo4 += 1
    if valores_corretos[i] % 5 == 0:
        multiplo5 += 1
print(f'{multiplo2} Multiplo(s) de 2')
print(f'{multiplo3} Multiplo(s) de 3')
print(f'{multiplo4} Multiplo(s) de 4')
print(f'{multiplo5} Multiplo(s) de 5')
