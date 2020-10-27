def funcao(x):
    y=int(input("Entrada 2 "))
    z=(x*y)+5
    if z <= 0:
        resposta = 'A'
    elif z <= 100:
        resposta = 'B'
    else:
        resposta = 'C'
    print(resposta)

valor=int(input("Entrada 1 "))
funcao(valor)
