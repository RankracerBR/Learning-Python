dna_1 = input()
dna_2 = input()
hamming = 0
valida = True

if dna_1 != dna_2:
    if len(dna_1) == len(dna_2):
        for i in range(len(dna_1)):
            if(dna_1[i]== 'A' or dna_1[i]=='C' or dna_1[i] == 'G' or dna_1[i] == 'T' ) and (dna_2[i]== 'A' or dna_2[i]=='C' or dna_2[i] == 'G' or dna_2[i] == 'T' ):
                if dna_1[i] != dna_2[i]:
                    hamming += 1  
            else:
                print('Cadeia de DNA inválida')
                valida = False
                break 
        if(valida == True):
            if hamming == len(dna_1):
                print('Cadeias de DNA completamente diferentes')
                
    else:
        print('Cadeias de DNA com tamanhos diferentes')
        print(f'A distância de Hamming = {hamming}')
else:
    print('Cadeias de DNA idênticas')