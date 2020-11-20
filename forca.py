print("""
-------------------Jogo da Forca-----------------

""")
palavra_chave='QUADRADO'
acertou=False
enforcou=False
while(not acertou and not enforcou):
    chute=input("Qual a letra? ")

    posicao=0
    for letra in palavra_chave:
        if chute.upper() == letra.upper():
            print("Encontrou a letra {} na posição {}".format(letra,posicao))
        posicao += 1
    print("Jogando")


print("Fim do jogo")