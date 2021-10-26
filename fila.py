def fila():
    fila = []
    while(True):
        print("\n1-Entrou um cliente na fila")
        print("2-Cliente atendido")
        print("3-Tamanho da fila")
        print("4-Fim do expediente")
        entrada = int(input("==>"))
        
        if entrada == 1:
            nome = str(input("\nNome do cliente: "))
            fila.append(nome)
        elif entrada == 2:
            print("\nCliente feliz...")
            fila.pop(0)
        elif entrada == 3:
            print("\n" , fila)
        elif entrada == 4:
            del fila[:]
            print("\n" , fila)
            break
        else:
            print("\nOpção inválida!")


print("=========Atendimento ao Cliente============")
fila()