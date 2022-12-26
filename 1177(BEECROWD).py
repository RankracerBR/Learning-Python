T = int(input())

a = []

for i in range(1000):
    j = 0
    while j < T: 
        a.append(j)
        j += 1
    print(f'N[{i}] = {a[i]}')