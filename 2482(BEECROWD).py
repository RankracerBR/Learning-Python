n = int(input())

dict = {}

while n > 0:
    n -= 1
    lingua = input()
    trad = input()
    dict[lingua] = trad
    
m = int(input())

while m > 0:
    m -= 1
    pessoa = input()
    lingua = input()
    print(pessoa)
    print(dict[lingua])
    print()