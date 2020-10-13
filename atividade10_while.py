print("----------------Cardápio-----------------")
print("")
print("Especificação    Código     Preço")
print("Cachorro Quente   200      R$ 10,50")
print("Bauru Simples     201      R$ 7,50")
print("Bauru com ovo     202      R$ 8,50")
print("Hambúrguer        203      R$ 15,50")
print("Cheeseburguer     204      R$ 16,50")
print("Refrigerante      205      R$ 5,00")
print("-"*40)

opc = []
c = 0
soma=0
pedido = 1

while pedido != 0:
    pedido = int(input("Codigo do pedido: "))
    if pedido == 200:
        c = 10.50
    if pedido == 201:
        c = 7.50
    if pedido == 202:
        c = 8.50
    if pedido == 203:
        c = 15.50
    if pedido == 204:
        c = 16.50
    if pedido == 205:
        c = 5
    qtd = int(input("Quantidade: "))
    valor = c * qtd
    opc.append(valor)
    i=str(input("Continuar? "))
    if i == "n":
        soma= sum(opc)
        print("Valor da compra: {0:.2f}".format(soma))
        break