lista=[]
soma_salario=0
soma_filhos=0
mediaS=0
mediaF=0
salario=0
j=0
m=0
n=0
per=0
while salario >= 0:
    salario=float(input("Salário: R$"))
    if salario < 0:
        break
    elif salario >= 0 and salario < 150:
        m = m + 1
    lista.append(salario)
    soma_salario = soma_salario + salario
    nf=int(input("Número de filhos: "))
    soma_filhos = soma_filhos + nf
    j += 1
mediaS= soma_salario/j
mediaF= soma_filhos/j
n = m*100
per = n/j
print("Média do salário da população é R${:.2f} ".format(mediaS))
print("Média de filhos é {:.2f}".format(mediaF))
print("O percentual de salários abaixo de R$150,00 são {:.1f}%".format(per))
print("O maior salário é de R${:.2f}".format(max(lista)))