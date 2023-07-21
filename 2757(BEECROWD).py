num1 = int(input())
num2 = int(input())
num3 = int(input())

print('A = %d, B = %d, C = %d' % (num1, num2, num3))
print('A = %10.0d, B = %10d, C = %10d' % (num1, num2, num3))
print('A = %s, B = %s, C = %s' % (str(num1).zfill(10), str(num2).zfill(10), str(num3).zfill(10)))
print('A = {:<10}, B = {:<10}, C = {:<10}'.format(num1, num2, num3))