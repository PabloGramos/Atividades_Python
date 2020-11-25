def jogar(chave):
    acertou = False
    enforcou = False
    erros = 0
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    print(letras_acertadas)
    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")
        if chute.upper() in chave:
            posicao = 0
            for letra in palavra_chave:
                if chute.upper() == letra.upper():
                    letras_acertadas[posicao] = letra
                posicao = posicao + 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("\nVocê ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")




print("""
-------------------Jogo da Forca-----------------

""")
palavra_chave='BANANA'
jogar(palavra_chave)

