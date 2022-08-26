conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6 ,7 ,8} #em conjunto mesmo se tiver um número repetido ele não irá mostrar a duplicidade do 5
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2) #intersection só irá mostrar números em ambos conjuntos 
print(conjunto_interseccao)
conjunto_diferenca = conjunto.difference(conjunto2) #difference só irá mostrar os números diferentes dos conjuntos
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2 ,3 ,4 ,5}
conjunto_subset = conjunto_a.issubset(conjunto_b) #issubset verifica se ambos conjuntos possuem os mesmos elementos
print('A é subconjunto de B: {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a) #issuperset verifica se completa os elementos em de B em A
print('B é um superconjunto de A: {}'.format(conjunto_superset))

lista = ['Cachorro', 'Cachorro', 'Gato', 'Gato', 'Elefante']
conjunto_animais = set(lista) #set remove a duplicidade dos elementos
print(conjunto_animais)
lista_animais = list(conjunto_animais)#list transforma em lista
print(lista_animais)

#conjunto = {1, 2 ,3 ,4, 4}
#conjunto.add(5)
#conjunto.discard(2)
#print(conjunto)