from revisao_matrizes import *

notas = obter_notas()

mostrar_notas(notas)

print(f'Maior nota: {maior_nota(notas)}')
print(f'Médias: {medias(notas)}')
print(f'Maior média: {maior_media(notas)}')
print(f'Total de aprovações: {quantidade_de_aprovacoes(notas)}')