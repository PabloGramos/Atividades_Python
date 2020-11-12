def valordepagar(n,d):
    valor_final=0
    dias = n * 0.012
    j=0
    while j < d:
        valor_final = valor_final + dias
        j += 1
    multa = n * 0.038
    valor_final = valor_final + n + multa
    print("Multa de R${} ".format(multa))
    print("Multa por dia de atraso R${} ".format(dias))
    print("Valor a ser pago R${:.2f} ".format(valor_final))

i=1
while i > 0:
    valor=float(input("Valor da prestação: R$"))
    atraso=int(input("Dias de atraso: "))
    if atraso > 0:
        valordepagar(valor,atraso)
    else:
        print("Valor a ser pago R${}".format(valor))
    i=int(input("1-Continuar 0-Sair "))
