colocacao = int(input())

if colocacao <= 1:
    print('Top 1')
elif colocacao <= 3:
    print('Top 3')
elif colocacao <= 5:
    print('Top 5')
elif colocacao <= 10:
    print('Top 10')
elif colocacao <= 25:
    print('Top 25')
elif colocacao <= 50:
    print('Top 50')  
else:
    print('Top 100')  
