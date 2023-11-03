t = int(input())

for i in range(0,t):
    pa,pb,g1,g2 = map(float, input().split())

    ano = 0
    while pb >= pa:
        pa = int(pa*(1 + g1/100))
        pb = int(pb*(1 + g2/100))

        ano += 1
        if ano >= 101:
            print('Mais de 1 seculo.')
            break

    if ano <= 100:
        print(f'{ano} anos.')