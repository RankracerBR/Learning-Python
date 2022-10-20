s = input()
b = 0
for x in range(len(s)):
    if s[x] == '1':
        b += 1

if b % 2 == 1:
    s += '1'
else:
    s += '0'

print(s)