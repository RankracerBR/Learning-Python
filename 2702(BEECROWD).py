n = [int(x) for x in str(input()).split()]
j = [int(x) for x in str(input()).split()]

soma = 0

if j[0] > n[0]: soma+= j[0] - n[0]
if j[1] > n[1]: soma += j[1] - n[1]
if j[2] > n[2]: soma += j[2] - n[2]

print(soma)