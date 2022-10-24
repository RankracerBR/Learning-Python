alunos_cpp = set([('João',11), ('Maria',33), ('José',44), ('Fulano',55), ('Beltrano',66)])
alunos_py = set([('Ana',31),('Diego',77),('Sebastião',88),('Fulano',100),('Beltrano',66)])

alunos_repetidos = alunos_cpp.intersection(alunos_py) #O intersection retorna informações informações repetidas
alunos_geral = alunos_cpp.union(alunos_py)

print(f'Existem {len(alunos_repetidos)} alunos nas duas turmas')
print(sorted(alunos_repetidos))

print(f'Existem {len(alunos_geral)} alunos no total')
print(sorted(alunos_geral))