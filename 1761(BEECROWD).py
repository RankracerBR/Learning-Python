import math

while True:
    try:
        A, B, C = map(float, input().split())
        altura_arvore = (B * math.tan(math.radians(A))) + C
        cordoes = round(5 * altura_arvore, 2)
        print(f'{cordoes:.2f}')
    except EOFError:
        break
