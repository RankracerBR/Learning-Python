T = int(input())
letras = ['a','A','e','E','i','I','o','O','s','S']

while T > 0:
    T -= 1 
    L = input()
    cont = 1
    for i in range(len(L)):
        if L[i] in letras:
            cont *= 3
        else:
            cont *= 2
            
    print(cont)