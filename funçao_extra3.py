def login():
    s=9999
    senha=int(input("Senha: "))
    if senha == s:
        print("Acesso permitido! ")
    else:
        print("Senha incorreta! ")



u=1234
usuario=int(input("Usuario: "))
if usuario == u:
    login()
else:
    print("Usuário inválido!")