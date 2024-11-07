'''
Faça um Programa que peça as quatro notas de 3 alunos, calcule 
e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0
'''
notas_alunos = []

for aba in range (3):
    notas = []
    print(f"aluno {aba + 1}: ")

    for k in range (4):
        nota = float(input(f"digite a nota { k + 1}: "))
        notas.append(nota)

    notas_alunos.append(notas)


medias = []

alunos_acima = 0 

for notas in notas_alunos:
    media = sum(notas) / len(notas)
    medias.append(media)

    if media >= 7.0:
        alunos_acima += 1

for aba in range(3):
    print(f"\nNotas do Aluno {aba + 1}: {notas_alunos[aba]}")
    print(f"Média do Aluno {aba + 1}: {medias[aba]}")

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {alunos_acima}")
