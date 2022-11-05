import math

def maior_nota(matriz):
    maiores = []
    for linha in matriz:
        maior = max(linha)
        maiores.append(maior)
    return max(maiores)

def medias(matriz):
    valores = []
    for linha in matriz:
        media = sum(linha) / len(linha)
        valores.append(math.floor(media))
    return valores

def maior_media(matriz):
    valores = medias(matriz)
    return max(valores)
def maior_quantidade_de_notas(matriz):
    valores = []
    for linha in matriz:
        valores.append(len(linha))
    return max(valores)
      
def mostrar_notas(matriz):
    print('Notas: ')
    quantidade = maior_quantidade_de_notas(matriz)
    for i in range(quantidade):
        print(f'{i+1}ª'.center(5), end = ' ')
    print()
    for lista in matriz:
        for n in lista:
            print(f'{n}'.center(5), end = ' ')
        print()
    print()
    
def obter_notas():
  matriz = []
  N = int(input('Informe a quantidade de disciplinas: '))
  for i in range(N):
    notas_str = input(f'Informe as notas da {i+1}ª disciplina: ')
    notas = []
    for nota in notas_str.split():
      notas.append(float(nota))
    matriz.append(notas)
  return matriz

def quantidade_de_aprovacoes(matriz):
    contador = 0
    notas = medias(matriz)
    for nota in notas:
        if nota >= 70:
            contador += 1
    return contador