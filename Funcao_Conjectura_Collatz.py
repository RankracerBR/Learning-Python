def conjectura_collatz(n):
    passos = 0
    while n != 1:
        if n % 2 == 0:
            passos = passos + 1
            n = n // 2
        
        else: 
            n = (n*3) + 1
            passos = passos + 1
    return passos