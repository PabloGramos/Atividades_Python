valor = float(input("Valor da compra: R$"))

if valor < 10.00:
    print('Lucro de 70%')
elif valor < 30.00 and valor >=10.00:
    print('Lucro de 50%')
elif valor < 50.00 and valor >=30.00:
    print('Lucro de 40%')
else:
    print('Lucro de 30%')