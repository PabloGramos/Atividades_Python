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
    _total_contas = 0
    def __init__(self,numero,titular,saldo=0.0,limite=1000.0):
        print('Iniciando a conta')
        self.numero=numero
        self.titular=titular
        self._saldo = saldo
        self.limite=limite
        self.historico = Historico()
        Conta._total_contas += 1

    def deposita(self, valor):
        self._saldo += valor
        self.historico.transacoes.append("deposito de {}".format(valor))

    def saca(self,valor):
        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))

    def extrato(self):
        print("Numero: {}\nExtrato: {}".format(self.numero,self._saldo))
        self.historico.transacoes.append("tirou extrato de {}".format(self.saldo))

    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True
    #  PROPERTY
    def saldo(self):
        return self._saldo
    # SALDO.SETTER
    def saldo(self,saldo):
        if(self._saldo < 0):
            print("saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def pega_saldo(self):
        return self.saldo

cliente = Cliente('Joao', 'Oliveira', '1111111111-1')
minha_conta = Conta('123-4', cliente, 1000.0)
novo_saldo = -200
if(novo_saldo < 0):
    print("Saldo inválido")
else:
    minha_conta.saldo = novo_saldo
conta = Conta('123-4','João',400.0)
conta2 = Conta('123-5','samuel',200.0)
print(conta._total_contas,' --- ',conta2._total_contas)
print("{}\n{}\n{}\n{}".format(conta.numero,conta.titular,conta.saldo,conta.limite))
conta.deposita(20.0)

print("Novo saldo apos deposito: ",conta.saldo,' ',minha_conta.pega_saldo())
conta.saca(100.0)
print("Novo saldo apos saque: ",conta.saldo)
conta.extrato()
print("Transderido R$300.00")
