N = input()
x = N.split(' ')
v = int(x[0])

for i in range(int(x[1])):
    a = input()

    if a == 'fechou':
        v += 1
    elif a == 'clicou':
        v -= 1

print(v)