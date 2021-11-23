def estante():
    fila = [[],[],[],[]]
    l = 0
    while(True):
        print("\n1 - Adicionar Livro na Estante")
        print("2 - Remover Livro da Estante")
        print("3 - Mostrar Livros na Estante")
        print("4 - Sair")
        opc = int(input("===> "))
        if opc == 1:
            if len(fila[0]) == 50:
                print("\nImpossível colocar!\n")
            else:
                codigo = int(input("Informe o código do livro: "))
                if codigo in fila[0]:
                    print("\nCódigo Invalido! ")
                else:
                    fila[0].append(codigo)
                    titulo = str(input("Informe o titulo do livro: "))
                    fila[1].append(titulo)
                    editora = str(input("Informe a editorta do livro: "))
                    fila[2].append(editora)
                    isbn = int(input("Digite o ISBN do livro: "))
                    fila[3].append(isbn)
        
        elif opc == 2:
            remove = int(input("Digite o código do livro a ser removido: "))
            if remove in fila[0]:
                for i in fila[0]:
                    if i == remove:
                        del fila[0][0]
                        del fila[1][0]
                        del fila[2][0]
                        del fila[3][0]
                        break
                    else:
                        del fila[0][0]
                        del fila[1][0]
                        del fila[2][0]
                        del fila[3][0]
            else:
                print("\nO livro não está na estante!\n")
        
        elif opc == 3:
            print("\nEstante==============")
            for j in fila[1]:
                l += 1
                print("Livro ", l ,": ", j)
        
        elif opc == 4:
            break
            
        
        else:
            print("\nOpção Inválida!\n")

print("___________LIVROS__NA__ESTANTE__________")
estante()