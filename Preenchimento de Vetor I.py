v = int(input())
n = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(n)):
    n[i] = v
    v = v*2
    print(f"N[{i}] = {n[i]}")