class Calculadora: 

        def __init__(self):
            pass 
        def soma(self, valor_a, valor_b):
            return valor_a + valor_b

        def subtracao(self, valor_a, valor_b):
            return valor_a - valor_b

        def multiplicacao(self, valor_a, valor_b):
            return valor_a * valor_b
        
        def divisao(self, valor_a, valor_b):
            return valor_a / valor_b

if __name__ == '__name__':
    calculadora = Calculadora(10, 2)
    print(calculadora.soma(10, 2))
    print(calculadora.subtracao(5, 3))
    print(calculadora.divisao(100, 2))
    print(calculadora.multiplicacao(10, 5))