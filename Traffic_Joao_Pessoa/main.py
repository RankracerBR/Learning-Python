import os 
import funcoes as fn
from dados import joao_pessoa
print(joao_pessoa)

while True:
    os.system('cls')
    opcao = fn.exibir_menu()
    if opcao == 1:
        fn.adicionar_bairro(joao_pessoa)
    if opcao == 2:
        fn.adicionar_rua(joao_pessoa)
    if opcao == 3:
        fn.exibir_dados(joao_pessoa)
    if opcao == 4:
        fn.exibir_rua_bairro(joao_pessoa)
    if opcao == 5:
        fn.calculo_trafego_bairro(joao_pessoa)
    if opcao == 6:
        fn.trafego_total(joao_pessoa)
    if opcao == 0:
        break
    print('\n') 
    input('Pressione ENTER para continuar...')