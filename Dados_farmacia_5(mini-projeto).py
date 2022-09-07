import os
import time

tamanho = os.get_terminal_size()
largura = tamanho[0]

sem_tarja =['Dipirona','Eno','Torsilax','Anador','Paracetamol']

tarja_amarela =['Cetoconazol','Amoxicilina','Febarbital','Carbamazepin','Ternoxicam']

tarja_vermelha =['Clavulanato','Ivermectina','Aziltromicina','Ampicilina','Amoxil']

tarja_preta =['Dimorf','Rivotril','Ritalina','Lexotan','Frisium']

tarjas =  ["Sem tarja","Tarja_amarela", "Tarja_vermelha", "Tarja_preta"]

precos = ['R$ 5,00','R$ 10,00','R$ 12,00','R$ 15,00']

op = 1

while op != 0:
    print('_'*200)
    print('Jampy'.center(largura))
    print('Menu de opções: ')
    print('1-Procurar remédio, 2-Ver tarjas, 3-Mostrar Remédios com as Tarjas, 4-Tabela de preços, 5-Fechar o programa')
    print('_'*200)
    pedido = int(input('Olá, seja bem-vindo a Farmácia Jampy, posso ajudar:(selecione as seguintes opções acima digitando um número): '))


    if pedido == 1:  
        print('\nTemos os seguintes remédios: ')
        print(f'{sem_tarja}')
        print(f'{tarja_amarela}')
        print(f'{tarja_vermelha}')
        print(f'{tarja_preta}')
        print('Aguarde alguns segundos')
        time.sleep(12) 
    
    elif pedido == 2:
       print('\nTemos as seguintes tarjas: {}'.format(tarjas)) 
       print('Aguarde alguns segundos')
       time.sleep(12)  
    
    elif pedido == 3:
        print('\nRemédios com suas respectivas Tarjas: ')
        print(f'{tarjas[0]}: {sem_tarja}')
        print(f'{tarjas[1]}: {tarja_amarela}')
        print(f'{tarjas[2]}: {tarja_vermelha}')
        print(f'{tarjas[3]}: {tarja_preta}')
        print('Aguarde alguns segundos')
        time.sleep(12)
    
    elif pedido == 4:
      print('\nTabela de Preços: ')  
      print(f'{precos[0]}/ {tarjas[0]}: {sem_tarja}')  
      print(f'{precos[1]}/ {tarjas[1]}: {tarja_amarela}')
      print(f'{precos[2]}/ {tarjas[2]}: {tarja_vermelha}')
      print(f'{precos[3]}/ {tarjas[3]}: {tarja_preta}')  
      time.sleep(12)
        
    elif pedido == 5:
        print('Até breve')
        break
    
    else: 
        print('Comando errado, digite novamente: ')
         