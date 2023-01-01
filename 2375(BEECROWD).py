n = int(input())

a,l,p = input().split(' ')

if n <= int(a) and  n <= int(l) and n <= int(p):
    print('S')
else:
    print('N')