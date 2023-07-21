def main():
    n = int(input().strip())
    ans = 0
    
    for _ in range(n):
        c,x = input().split()
        x = int(x)
        if c == 'G':
            ans -= x 
        else:
            ans += x
    
    if ans >= 0:
        print("A greve vai parar.")
    else:
        print("NÃO VAI TER CORTE, VAI TER LUTA!")
    
if __name__ == "__main__":
    main()