def f(x):
  y = x**2
  return y 

x = float(input('Informe o valor de x: '))
y = f(x)
print(f'f({x} = {y})')
h = 0.000001
dx = (f(x+h) - f(x)) / h
print(f"f'({x}) = {dx}")