x = [1,5,2,6,3,7]

media = sum(x) / len(x)
print(media)

mediana = sorted(x)
indice = len(mediana)
meio = indice // 2

if indice % 2 == 0:
    mediana = (mediana[meio-1] + mediana[meio]) / 2
else:
    mediana = mediana[meio]
print(mediana)
