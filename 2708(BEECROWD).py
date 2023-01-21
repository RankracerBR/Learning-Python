turistas = 0
jipe = 0
while True:
    n = input().split()
    if n[0] == 'ABEND':
        break 
    if n[0] == 'SALIDA':
        jipe += 1
        turistas += int(n[1])
    else:
        jipe -= 1
        turistas -= int(n[1])
    
print(turistas)
print(jipe)
        