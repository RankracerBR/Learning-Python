F1,F2 = map(float, input().split())
PIB = (100.00+F1)*(F2/100.00+1) - 100.00
print(f'{PIB:.6f}')