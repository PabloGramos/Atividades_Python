import datetime
class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprime(self):
        print("data abertura: {}".format(self.data_abertura))
        print("transações: ")
        for t in self.transacoes:
            print("-",t)

class Cliente:
    def __init__(self,nome,sobrenome,cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self,numero,titular,saldo,limite=1000.0):
        print('Iniciando a conta')
        self.numero=numero
        self.titular=titular
        self.saldo=saldo
        self.limite=limite
        self.historico = Historico()

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("deposito de {}".format(valor))

    def saca(self,valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))

    def extrato(self):
        print("Numero: {}\nExtrato: {}".format(self.numero,self.saldo))
        self.historico.transacoes.append("tirou extrato de {}".format(self.saldo))

    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True

    def pega_saldo(self):
        return self.saldo

cliente = Cliente('Joao', 'Oliveira', '1111111111-1')
minha_conta = Conta('123-4', cliente, 1000.0)
novo_saldo = -200
if(novo_saldo < 0):
    print("Saldo inválido")
else:
    minha_conta.saldo = novo_saldo
conta = Conta('123-4','João',120.0)
print("{}\n{}\n{}\n{}".format(conta.numero,conta.titular,conta.saldo,conta.limite))
conta.deposita(20.0)

print("Novo saldo apos deposito: ",conta.saldo,' ',minha_conta.pega_saldo())
conta.saca(150.0)
print("Novo saldo apos saque: ",conta.saldo)
conta.extrato()
print("Transderido R$300.00")
