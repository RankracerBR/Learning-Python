# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

n1,n2,n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
  maior = n1
elif n2 > n1 and n2 > n3:
  maior = n2
else:
  maior = n3

if n1 < n2 and n1 < n3:
  menor = n1
elif n2 < n1 and n2 < n3:
  menor = n2
else:
  menor = n3

if n1 != maior and n1 != menor:
  meio = n1
elif n2 != maior and n2 != menor:
  meio = n2
else:
  meio = n3

print(menor)
print(meio)
print(maior)
print()
print(n1)
print(n2)
print(n3)