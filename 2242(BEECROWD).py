entrada = input()
vogais = ""
for l in entrada:
    if(l=="a"or l== "e" or l =="i" or l=="o"or l=="u"):
        vogais+=l 
if (vogais == vogais[::-1]):
    print("S")
else:
    print("N")