from sympy import fu


turma = dict() #dict = Dicionário 

turma['Fulano'] = [50,70,40]
turma['Beltrano'] = 70
turma['Mária'] = 100

nome = input('Informe o nome do aluno: ')
indice = int(input('Informe quais das primeiras notas queira receber: '))
indice -= 1 

if nome in turma: 
    print(turma[nome][indice])
if nome not in turma or indice not in turma: 
    print('Erro! algum dos dados estão errados')
    print('Os nomes e as notas devem ser: ')
    print(f'{turma}')