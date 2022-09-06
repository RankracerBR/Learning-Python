import os

tamanho = os.get_terminal_size()
largura = tamanho[0]

sem_tarja =['Dipirona','Eno','Torsilax','Anador','Paracetamol']

tarja_amarela =['Cetoconazol','Amoxicilina','Febarbital','Carbamazepin','Ternoxicam']

tarja_vermelha =['Clavulanato','Ivermectina','Aziltromicina','Ampicilina','Amoxil']

tarja_preta =['Dimorf','Rivotril','Ritalina','Lexotan','Frisium']

tarjas =  ["sem tarja","tarja_amarela", "tarja_vermelha", "tarja_preta"]

conjunto_1 = [sem_tarja,tarja_amarela,tarja_vermelha,tarja_preta]
conjunto_2 = [tarjas]
op = 1



while op != 0:
    print('_'*200)
    print('Jampy'.center(largura))
    print('Menu de opções: ')
    print('1-Procurar remédio, 2-Ver tarjas, 3-sair')
    print('_'*200)
    pedido = int(input('Olá, seja bem-vindo a Farmácia Jampy, posso ajudar:(pressiona 1, 2 ou 3 para selecionar): '))

    
    
    if pedido == 1:
       print('Temos os seguintes remédios: ')
       print(f'{sem_tarja}') 
       print(f'{tarja_amarela}') 
       print(f'{tarja_vermelha}')
       print(f'{tarja_preta}') 
    elif pedido == 2:
       print('Temos as seguintes cargas: {}'.format(conjunto_2)) 

    elif pedido == 3:
        
        print('Até breve')
        break
    else: 
        print('Comando errado, digite novamente: ')