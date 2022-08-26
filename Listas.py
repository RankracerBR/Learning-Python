lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

#tuple é imutável e converte os valores
#[] = lista 
#() = tupla


tupla = (1, 10, 12, 14)
print(len(tupla)) #len = length(tamanho)
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
lista_numerica[0] = 100
print(lista_numerica)















#lista.sort() #sort ordena a lista
#lista_animal.sort()
#print(lista)
#print(lista_animal)
#lista_animal.reverse() #reverse = reverter 
#print(lista_animal)

#print(lista_animal[1])
#print(sum(lista)) # método mais fácil para somar os números da lista
#print(max(lista))
#print(min(lista))
#print(min(lista_animal))
#print(max(lista_animal))

#nova_lista = lista_animal * 3 #repete os número pela quantidade multiplicada
#print(nova_lista)

#if 'lobo' in lista_animal:
 #   print('existe um gato na lista')
#else:
 #   print('não existe um lobo na lista. Será incluido')
  #  lista_animal.append('lobo')#append inclui na lista alguma informação a mais não decladara anteriormente
   # print(lista_animal)

#lista_animal.pop(0) #pop retira o elemento da lista
#print(lista_animal)
#lista_animal.remove('elefante')
#print(lista_animal)



#soma = 0 #irá somar todos os elementos de cada uma vez
#for x in lista:
 #   print(x)
  #  soma += x 
   # print(soma)