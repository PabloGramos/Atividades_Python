pilha = []
i=1
while True:
    valores = int(input("Digite um valor para a pilha: "))
    pilha.append(valores)
    i += 1
    cont = int(input("Adicionar mais?(1-Sim/0-Não: )"))
    if cont == 0:
        break
    print("")
    
    
while True:
    print("\nPilha atual: ", pilha, "\n")
    
    print("1 - Adicionar à pilha")
    print("2 - Remover da pilha")
    print("3 - Encerrar")
    opc = int(input("==> "))
    
    if opc == 1:
        valor = int(input("Digite o valor para ser adicionado: "))
        pilha.append(valor)
    
    elif opc == 2:
        if len(pilha) == 0:
            print("Sem valores para ser removidos!")
            break
        
        print("\nValor removido")
        pilha.pop()
    
    elif opc == 3:
        print("\nResultado final da pilha: ", pilha)
        break
    
    else:
        print("\nOpção inválida!")
        break