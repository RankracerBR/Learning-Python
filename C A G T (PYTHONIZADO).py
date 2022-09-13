dna_1 = input()
dna_2 = input()
hamming = 0
valida = True 
letras = 'ACGT'

if dna_1 != dna_2:
    if len(dna_1) == len(dna_2):
        for l1, l2 in zip(dna_1,dna_2):
            if l1 in letras and l2 in letras:
                if l1 != l2:
                    hamming += 1 
            else:
                print('Cadeia de DNA inválida')
                valida = False 
                break 
            if(valida == True):
                if hamming == len(dna_1):
                    print('Cadeias de DNA completamente diferentes')
                else:
                    print('Cadeias de DNA com diferenças')
                    print(f'A distância de Hamming = {hamming}')
            else:
                print('Cadeias de DNA com tamanhos diferentes')
        else:
             print('Cadeias de DNA idênticas')