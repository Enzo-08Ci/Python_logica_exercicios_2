"""
7. Lista de Alunos

Crie uma lista contendo nomes de alunos.

Percorra a lista exibindo:

Aluno: Maria
Aluno: João
Aluno: Pedro
"""

names = ["Enzo", "Camila", "Willian", "Bruna"]

print("\nNomes:\n")
for name in names:
    print(f'Aluno: {name}')

print("\nNúmeros e nomes:\n")

cont = 1
for name in names:
    print(f'{cont} - {name}')
    cont +=1