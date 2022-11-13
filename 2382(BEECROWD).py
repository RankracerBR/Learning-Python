import math 
l ,a,p,r = map(int, input().split())
r=r+r
diagonal = math.sqrt((l*l)+(a*a)+(p*p))
if diagonal <= r:
    print('S')
else:
    print('N')                   

