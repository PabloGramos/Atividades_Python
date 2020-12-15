class Funcionario:
    def __init__(self , nome , cpf , salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

class Gerente(Funcionario):
    def __init__(self, senha, qtd_gerenciados):
        Funcionario.__init__(nome,cpf,salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

    def autentica(self,senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False