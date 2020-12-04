s = 1
x = 1
soma = 0
produto = 0

print("*----------EletroSell----------*")
for produto in range(x >= 0):
    produto = float(input("Digite o valor do produto: R$"))
    if produto == 0:
        break
    else:
        s += 1
        soma += produto
print("Total: {0:.2f}R$".format(soma))
dinheiro = float(input("Dinheiro: R$ "))
dinheiro -= soma
print("Troco: R${0:.2f}".format(dinheiro))
