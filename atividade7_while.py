notas = []
soma=0
i=1
cand=int(input("Numero de candidatos: "))
while i <= cand:
    i += 1
    nome=str(input("Nome do candidato: "))
    n1=int(input("Nota 1 "))
    notas.append(n1)
    n2=int(input("Nota 2 "))
    notas.append(n2)
    n3 = int(input("Nota 3 "))
    notas.append(n3)
    n4 = int(input("Nota 4 "))
    notas.append(n4)
    n5 = int(input("Nota 5 "))
    notas.append(n5)
    n6 = int(input("Nota 6 "))
    notas.append(n6)
    n7 = int(input("Nota 7 "))
    print(" ")
    notas.append(n7)
    print("Candidato ",nome)
    print(notas)
    print("Maior nota {}".format(max(notas)))
    print("Menor nota {} ".format(min(notas)))
    notas.remove(min(notas))
    notas.remove(max(notas))
    print(notas)
    soma = sum(notas)
    print(soma)
    print("Media das notas é {}".format((soma)/5))
    if i > cand:
        break