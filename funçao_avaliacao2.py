def funcao():
    if sexo == 'm' or sexo == 'masculino':
        ideal = (72.7 * altura) - 58
    else:
        ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é {:.2f}".format(ideal))
sexo=str(input("Sexo masculino(m) ou feminino(f)? "))
nome=str(input("Qual é o seu nome? "))
altura=float(input("Digite sua altura: "))
funcao()







