x = int(input())
dentro = 0
fora = 0
for a in range(1, x + 1):
    b = int(input())
    if b >= 10 and b <= 20:
        dentro = dentro + 1
    else: 
        fora = fora + 1
print(f'{dentro} in')
print(f'{fora} out')