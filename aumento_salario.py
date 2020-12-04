salario = float(input("Digite seu salário bruto: "))
novo = 0

if salario <= 1045.00:
    print("Seu salário é: ", salario)
    print("Seu salário foi isento")
    print("Seu salário aumentou para: ", salario)
elif salario <= 1900:
    print("Seu salário é: ", salario)
    print("Diminuição de 5% com o desconto")
    novo = salario - (salario*0.05)
    print("Seu novo salário é: ", novo)
elif salario <= 3500:
    print("Seu salário é: ", salario)
    print("Diminuição de 10% com o desconto")
    novo = salario - (salario*0.10)
    print("Seu novo salário é: ", novo)
else:
    print("Seu salário é: ", salario)
    print("Diminuição de 20% com o desconto")
    novo = salario - (salario*0.20)
    print("Seu novo salário é: ", novo)