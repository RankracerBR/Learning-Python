valor = input().split(' ')

A1, B1, C1 = valor

triangulo = ((float)(A1) * (float)(C1) )/2 
circulo = (3.14159*((float)(C1)*(float)(C1))) 
trapezio =((float)(C1) * ((float)(A1) + (float)(B1))) / 2
quadrado = ((float)(B1)* (float)(B1))
retangulo =((float)(A1) * (float)(B1))

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retangulo:.3f}')