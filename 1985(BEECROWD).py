N = int(input())

v = 0.0

for i in range(N):
    p = input().split(' ')
    if int(p[0]) == 1001:
        v += int(p[1]) * 1.50
    elif int(p[0]) == 1002:
        v += int(p[1]) * 2.50
    elif int(p[0]) == 1003:
        v += int(p[1]) * 3.50
    elif int(p[0]) == 1004:
        v += int(p[1]) * 4.50
    elif int(p[0]) == 1005:   
        v += int(p[1]) * 5.50

print(f'{v:.2f}')    
    