a = []
for i in range (5):
    n = int(input())
    a.append(int(n))

I = 0
m = 0
o = 0
p = 0

for j in range(5):
    if a[j] % 2 == 0:
        I += 1
    if a[j] % 2 == 1:
        m += 1
    if a[j] > 0:
        o += 1
    if a[j] < 0:
        p += 1

print(I,'Valor(es) Par(es)') 
print(m,'Valor(es) Impar(es)') 
print(o,'Valor(es) Positivo(s)') 
print(p,'Valor(es) Negativo(s)') 