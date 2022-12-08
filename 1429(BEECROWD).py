import math 

while True:
    v = input()
    acm = 0
    if v == '0':
        break
    v = v[::-1]
    
    for i,j in enumerate(v):
        acm += int(j) * int(math.factorial(i+1))
        
    print(acm)