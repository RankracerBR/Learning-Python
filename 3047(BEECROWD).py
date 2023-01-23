M = int(input())
A = int(input())
B = int(input())

x = M - A - B     

if x > A and x > B:
    print(x) 
elif A > B and A > x:
    print(A)
else:
    print(B)