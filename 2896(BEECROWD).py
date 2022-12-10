T = int(input())

while T > 0:
    T -= 1
    n,k = input().split()
    n = int(n)
    k = int(k)
    total = int(int(n % k) + int(n / k))
    print(total)
    