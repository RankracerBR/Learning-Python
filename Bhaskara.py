v = input().split()
a, b, c = v

a = float(a)
b = float(b)
c = float(c)

if a == 0.0  or (b ** 2 - 4 * a * c) < 0:
    print('Impossivel calcular')
else:
    bhaskara1 = (- b + (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    bhaskara2 = (- b - (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
    print(f'R1 = {bhaskara1:.5f}')
    print(f'R2 = {bhaskara2:.5f}' )