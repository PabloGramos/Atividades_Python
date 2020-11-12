soma=0
j=0
s=''
print("0 para encerrar...")
while j >= 0:
    j += 1
    idade=int(input("Diga sua idade: "))
    if idade == 0:
        break
    soma = soma + idade
media = soma/j
arquivo = open('meu_arquivo.txt','w')

if media>=0 and media<=25:
    print("Turma joven ")
    s='Turma jovem'
elif media>=26 and media<=60:
    print("Turma adulta ")
    s = 'Turma adulta'
else:
    print("Turma idósa ")
    s = 'Turma idósa'
arquivo.write('{}'.format(s))
arquivo.close()