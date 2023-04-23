a,b,c = map(float, input().split())
area = ((a+b)/2) * c
perimetro = a+b+c
if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print(f'Perimetro = {perimetro:.1f}')
else:
    print(f'Area = {area:.1f}')