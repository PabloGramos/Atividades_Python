def Empilhar_Containers():
    pilhas = [[],[],[],[],[]]
    status = ["Disponivel", "Disponivel", "Disponivel", "Disponivel"]
    i=0
    
    while(True):
        print("\n---------------------------")
        print("Espaço 1: ", status[0])
        print("Espaço 2: ", status[1])
        print("Espaço 3: ", status[2])
        print("Espaço 4: ", status[3])
        print("---------------------------")
    
        print("\n1 - Empilhar")
        print("2 - Desempilhar")
        print("3 - Sair")
        opc = int(input("==> "))
        
        if opc == 1:
            while(True):
                if i == 3:
                    i = 0
                if len(pilhas[i]) > len(pilhas[i+1]):
                    i += 1
                    
                if status[3] == "Cheio":
                    print("\n\nImpossivel Empilhar!\n")
                    break
                
                else:
                    codigo = int(input("\nCódigo do container: "))
                    if codigo in pilhas[0] or codigo in pilhas[1] or codigo in pilhas[2] or codigo in pilhas[3]:
                        print("\n\nCódigo Inválido!\n")
                    else:
                        pilhas[i].append(codigo)
                        if len(pilhas[i]) == 3:
                            status[i] = "Cheio"
                        break
                
                
        elif opc == 2:
            codigo=int(input("\nDigite o código que será removido:"))
            if codigo == pilhas[0][-1]:
                del pilhas[0][-1]
                if len(pilhas[0]) < 3:
                    status[i] = "Disponivel"
                    
            elif codigo == pilhas[1][-1]:
                del pilhas[1][-1]
                if len(pilhas[1]) < 3:
                    status[i] = "Disponivel"
                    
            elif codigo == pilhas[2][-1]:
                del pilhas[2][-1]
                if len(pilhas[2]) < 3:
                    status[i] = "Disponivel"
                    
            elif codigo == pilhas[3][-1]:
                del pilhas[3][-1]
                if len(pilhas[3]) < 3:
                    status[i] = "Disponivel"
                    
            else:
                print("\nImpossivél desempilhar!\n")
            
            
            
        elif opc == 3:
            print("\n\nLocal 1: ", pilhas[0])
            print("Local 2: ", pilhas[1])
            print("Local 3: ", pilhas[2])
            print("Local 4: ", pilhas[3])
            break
            
        else:
            print("Opção Inválida!")



print("****************************************************")
print("****************EMPILHAR CONTAINERS*****************")
print("****************************************************")

Empilhar_Containers()