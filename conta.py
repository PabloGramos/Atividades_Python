class Funcionario:
    def __init__(self , nome , cpf , salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10

class Gerente(Funcionario):
    def __init__(self,nome,cpf,salario, senha, qtd_gerenciados):
        super().__init__(nome,cpf,salario)
        self._senha = senha
        self._qtd_gerenciados = qtd_gerenciados

    def autentica(self,senha):
        if self._senha == senha:
            print("acesso permitido")
            return True
        else:
            print("acesso negado")
            return False
    def get_bonificacao(self):
        return self._salario * 0.15


gerente = Gerente('Jose','222222222-22',5000.0,'1234',0)
print(gerente.get_bonificacao())

funcionario = Funcionario('joao','111111111-11',2000.0)
print(funcionario.get_bonificacao())
print(vars(funcionario))
print(vars(gerente))