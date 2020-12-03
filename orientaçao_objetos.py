def cria_conta(numero,titular,saldo,limite):
    conta = {
    "numero" : numero,
    "titular" : titular,
    "saldo" : saldo,
    "limite" : limite
    }
    return(conta)

def deposita(conta,valor):
    conta['saldo'] += valor
    print(conta['saldo'])

def saca(conta,valor):
    conta['saldo'] -= valor
    print(conta['saldo'])

def extrato(conta):
    print("numero: {} \nsaldo: {}".format(conta['numero'],conta['saldo']))

#CORPO PRINCIPAL
conta1 = cria_conta('123-4',"Joao",120.0,1000.0)
conta2 = cria_conta('123-5',"Jose",200.0,1000.0)


print(conta1['numero'])
deposita(conta1,300.0)
saca(conta1,100.0)
extrato(conta1)
print(conta2['numero'])
deposita(conta2,400.0)
saca(conta2,200.0)
extrato(conta2)