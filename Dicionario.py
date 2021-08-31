
senha = {"senha" : 9876}
entrada = int(input("Senha: "))
if senha["senha"] == entrada:
    print("\nACESSO PERMITIDO")
else:
    print("\nACESSO NEGADO")
    

print("\n=================================")


vl1 = int(input("\nDigite um número: "))
vl2 = int(input("Digite outro número: "))

operacoes = {
    "adicao" : vl1 + vl2,
    "subtracao" : vl1 - vl2,
    "divisao" : vl1 / vl2,
    "multiplicacao" : vl1 * vl2,
}

print("\n1.Adição")
print("2.Subtração")
print("3.Divisão")
print("4.Multiplicação")
operacao = int(input("=> "))

if operacao == 1:
    print(vl1, " + " ,vl2, " = ",operacoes["adicao"])
elif operacao == 2:
    print(vl1, " - " ,vl2, " = ",operacoes["subtracao"])
elif operacao == 3:
    print(vl1, " / " ,vl2, " = ",operacoes["divisao"])
elif operacao == 4:
    print(vl1, " x " ,vl2, " = ",operacoes["multiplicacao"])
else:
    print("Opção não válida!")







