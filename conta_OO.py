class Conta:
    def __init__(self,numero,titular,saldo,limite):
        print('Iniciando a conta')
        self.numero=numero
        self.titular=titular
        self.saldo=saldo
        self.limite=limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self,valor):
        self.saldo -= valor
        return True

    def extrato(self):
        print("Numero: {}\nExtrato: {}".format(self.numero,self.saldo))

    def transfere(self, destino, valor):
        self.saldo -= valor
        destino.saldo += valor


conta = Conta('123-4','João',120.0,1000.0)
print("{}\n{}\n{}\n{}".format(conta.numero,conta.titular,conta.saldo,conta.limite))
conta.deposita(20.0)
print("Novo saldo apos deposito: ",conta.saldo)
conta.saca(30.0)
print("Novo saldo apos saque: ",conta.saldo)
conta.extrato()