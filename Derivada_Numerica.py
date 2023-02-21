def funcao(x):
    y = x**2
    return y 
def funcao_2(x):
    y = x**3
    return y
def derivada(f,x,h):
    dfdx = (f(x+h) - f(x))/h
    return dfdx

print(derivada(funcao,2.0,0.0001))
print(derivada(funcao_2, 2,0.001))
