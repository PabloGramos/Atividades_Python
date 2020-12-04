n = 1
turma = 1
soma = 0

q=int(input("Digite a quantidade de turmas: "))
print("  ")
print("Digite a quantidade de alunos por turmas até 35")
print("0 Para calcular a média")

while turma > 0:
    turma = int(input("Turma número {}: ".format(n)))
    soma = soma + turma
    n += 1;
print("Total de alunos ", soma)
print("O número médio de alunos por turma é ", soma / q)