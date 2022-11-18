Q = int(input())
alunos = dict()
for i in range(Q):
    consulta = input().split()
    if consulta[0] == '1':
        if consulta[1] in alunos:
            alunos[consulta[1]] += int(consulta[2])
        else:
            alunos[consulta[1]] = int(consulta[2])
    elif consulta[0] == '2':
        alunos[consulta[1]] == 0
    elif consulta[0] == '3':
        print(alunos[consulta[1]])