import random


def imprime_msg():
    print("""
    *************************************************
    -------------------Jogo da Forca-----------------
    *************************************************
    """)

def carrega_palavra():
    palavra_chave = ''
    arquivo = open('palavras.txt', 'r')
    lista = []
    for linha in arquivo:
        lista.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(lista))
    palavra_chave = lista[numero].upper()
    return palavra_chave


def jogar(chave):
    imprime_msg()

    acertou = False
    enforcou = False
    erros = 0

    letras_acertadas = ['_' for letra in palavra_chave]
    print(letras_acertadas)
    while (not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
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



# CORPO PRINCIPAL
palavra_chave = carrega_palavra()
jogar(palavra_chave)

