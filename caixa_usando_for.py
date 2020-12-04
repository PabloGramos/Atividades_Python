valor = 0
soma = 0
s = 1

print("---------- Super Lojas ----------")
for valor in range(0, 100):
    valor=float(input("Digite o valor {}; ou 0 para encerrar: R$" .format(s)))
    if valor == 0:
        break
    else:
        s += 1
        soma += valor

print('O valor total é R${0:.2f}'.format(soma))
pago=float(input('Valor pago: R$'))
troco=float(pago - soma)
print("Troco R${0:.2f} ".format(troco))