from Televisao import Televisao 
from contador_letras import contador_letras, teste
televisao = Televisao()
print(televisao.ligada)
televisao.power 
print(televisao.ligada)
lista = ['cachorro', 'gato', 'elefante']
total_letras = contador_letras(lista)
print('Total de letras por palavra de lista: {}'.format(total_letras))
print(teste())
print(contador_letras(lista))