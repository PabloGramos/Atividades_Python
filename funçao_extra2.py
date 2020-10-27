def alcool():
    litros = int(input("Digite a quantidade em litros: "))
    i = 0
    valor = 0
    while i < litros:
        i += 1
        valor = valor + 3.90
        if litros <= 20:
            valor = valor - 0.03
        else:
            valor = valor - 0.05
    print("Por {} litros de alcool o valor a pagar é {:.2f}. ".format(litros, valor))


def gasolina():
    i = 0
    valor = 0
    litros = int(input("Digite a quantidade em litros: "))
    while i < litros:
        i += 1
        valor = valor + 4.30
        if litros <= 20:
            valor = valor - 0.03
        else:
            valor = valor - 0.05
    print("Por {} litros de gasolina o valor a pagar é {:.2f}. ".format(litros, valor))


tipo = int(input("Digite 1 para Álcool ou 0 para Gasolina: "))
if tipo == 1:
    alcool()
elif tipo == 0:
    gasolina()
else:
    print("Opção invalida")