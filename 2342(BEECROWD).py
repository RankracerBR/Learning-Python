N = int(input())

v =  input().split()

if v[1] == '+':
    total = int(v[0]) + int(v[2])
else:
    total = int(v[0]) * int(v[2]) 
    
if total > N:
    print('OVERFLOW')
else:
    print('OK')
