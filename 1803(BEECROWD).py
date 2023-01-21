import sys

valores = [input() for i in range(4)]

c = "" 
d = ""  

for i in range(4):
    c += valores[i][0]
    d += valores[i][-1]

l = int(d)
k = int(c)

for i in range(1, len(valores[0])-1):
    a = ""
    for j in range(4):
        a += valores[j][i]
    r = int(a)
    sys.stdout.write(chr((k * r + l) % 257))

print()