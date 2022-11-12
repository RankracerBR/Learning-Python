n1 = int(input())
curso1 = set(input().split())
n2 = int(input())
curso2 = set(input().split())


repetidos = curso1.intersection(curso2)
alunos_geral = curso1.union(curso2)


print(f'existem {len(alunos_geral)} alunos no total nos dois cursos')
