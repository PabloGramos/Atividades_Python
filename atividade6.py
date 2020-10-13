n = 1
turma = 0
soma = 0

q=int(input("Digite a quantidade de turmas: "))
print("  ")
print("Digite a quantidade de alunos por turmas até 35")

for q in range(1,q+1):
    turma = int(input("Turma número {}: ".format(n)))
    soma = soma + turma
    n += 1;
print("Total de alunos ", soma)
print("O número médio de alunos por turma é ", soma / q)

