vezes = int(input())
numero = ['0','1','2','3','4','5','6','7','8','9']

for i in range(vezes):
    valor = list(input())
    
    for j in range(len(valor)):
        
        if not valor[j] in numero: 
            valor[j]=","
    lista=("".join(valor).split(","))
    lista2=[]
    for z in lista:
        if not z=="":
            lista2.append(int(z))
    print(sum(lista2))