salario = float(input("Digite seu salário: "))
novo_s = 0
aumento = 0

if salario <= 2800.00:
    print("Seu salário é: R$", salario)
    print("Aumento de 20%")
    novo_s = salario + (salario*0.2)
    aumento = salario*0.2
    print("Será aumentado: R$", aumento)
    print("Seu novo salário é: R$", novo_s)

elif salario >= 2800.00 and salario <= 7000.00:
    print("Seu salário é: R$", salario)
    print("Aumento de 15%")
    novo_s = salario + (salario*0.15)
    aumento = salario * 0.15
    print("Será aumentado: R$", aumento)
    print("Seu novo salário é: R$", novo_s)

elif salario >= 7000.00 and salario <= 15000.00:
    print("Seu salário é: R$", salario)
    print("Aumento de 10%")
    novo_s = salario + (salario*0.1)
    aumento = salario * 0.1
    print("Será aumentado: R$", aumento)
    print("Seu novo salário é: R$", novo_s)

else:
    print("Seu salário é: R$", salario)
    print("Aumento de 5%")
    novo_s = salario + (salario*0.05)
    aumento = salario * 0.05
    print("Será aumentado: R$", aumento)
    print("Seu novo salário é: R$", novo_s)