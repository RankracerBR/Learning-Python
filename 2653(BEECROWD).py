n = []

while True:
    try:
        n.append(input())
        
    except EOFError:
        break
        
n = set(n)
print(len(n))