b = int(input())
g = int(input())

if g % 2 !=0:
    g-=1
if g <= b*2:
    print('Amelia tem todas bolinhas!')
else:
    result = (g-(2*b)) / 2
    print(f'Faltam {result:.0f} bolinha(s)')