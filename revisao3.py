soma=0
j=0
print("0 para encerrar...")
while j >= 0:
    j += 1
    idade=int(input("Diga sua idade: "))
    if idade == 0:
        break
    soma = soma + idade
media = soma/j
if media>=0 and media<=25:
    print("Turma joven ")
elif media>=26 and media<=60:
    print("Turma adulta ")
else:
    print("Turma idósa ")