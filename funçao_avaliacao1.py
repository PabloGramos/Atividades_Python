i=0
def funcao():
        lista = []
        aprovacao = []
        ap = 'Aprovado'
        rp = 'Reprovado'
        rc = 'Recuperação'
        i=1
        j=0
        soma=0
        nome = str(input("Nome do {} aluno: ".format(i)))
        disciplinas = int(input("Numero de disciplinas: "))
        for d in range(disciplinas):
            j += 1
            nota = float(input("Nota da {} disciplina: ".format(j)))
            soma = soma + nota
        media = soma / j
        print("Média {:.2f}".format(media))
        lista.append(nome)
        lista.append(media)
        j = 0
        soma = 0
        if media >= 7:
            aprovacao.append(ap)
        elif media < 7 and media > 4:
            aprovacao.append(rc)
        else:
            aprovacao.append(rp)

        i = 0
        for al in range(alunos):
            print("Aluno-> ", lista[j])
            j = j + 1
            print("Média-> ", lista[j])
            print("Resultado-> ", aprovacao[i])
            i += 1
            j += 1


alunos=int(input("Quantidade de alunos no curso: "))
while i <= alunos:
    i += 1
    if i > alunos:
        break
    else:
        funcao()
