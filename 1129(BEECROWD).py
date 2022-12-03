contadorcontinuo = True
while contadorcontinuo:    
    numero = int(input())
    if numero != 0:
        for conadort in range(0,numero):
            cores = input()
            core = cores.split(" ")
            asterisco = "*"
            Marcador = 0
            for contador2 in range(0,5):
                analisador = int(cores[contador2])
                if analisador <= 127:
                    item = contador2+1
                    Marcador = Marcador+1
            if asterisco == 1:
                asterisco = "A"
            elif asterisco == 2:
                asterisco = "B"
            elif asterisco == 3:
                asterisco = "C"
            elif asterisco == 4:
                asterico = "D"
            elif asterisco == 5:
                asterisco = "E"
            if(Marcador >1):
                asterisco = "*"
            print(asterisco)
    elif numero == 0:
        contadorcontinuo= False