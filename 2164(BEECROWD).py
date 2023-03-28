import math

def fibonacci(x):
    return (math.pow((1+math.sqrt(5)) / 2.0,x)) - (math.pow((1-math.sqrt(5)) / 2.0, x))

n = int(input())
result = fibonacci(n)
print('{:.1f}'.format((result) / math.sqrt(5)))