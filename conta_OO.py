class Conta:
    def __init__(self,numero,titular,saldo,limite):
        self.numero=numero
        self.titular=titular
        self.saldo=saldo
        self.limite=limite

    pass

from conta import Conta
conta = Conta()
