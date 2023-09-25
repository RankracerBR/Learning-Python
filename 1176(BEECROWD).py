fibo = [0,1]

p=0
s=1

for i in range(60):
   t = s+p
   fibo.append(t)    
   p=s
   s=t

t = int(input())
for i in range(t):
    n = int(input())
    print('Fib(%d) = %d' %(n, fibo[n]))