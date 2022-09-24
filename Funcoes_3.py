import sympy as sp 
print('Calculadora de Derivada')
funcao = input('Informe a função a ser derivada')
var = input('Informe a variável a ser derivada')
exp = sp.sympify(funcao)
sp.pprint(exp)
print()
exp = sp.sympify('cos(x**2)')
sp.pprint(exp) #pretty print
dx = sp.Derivative(exp, 'x').doit()
sp.pprint(dx)