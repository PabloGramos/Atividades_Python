print("""
-------------------Jogo da Forca-----------------

""")
palavra_chave='BANANA'
acertou=False
enforcou=False
erros=0
letras_acertadas=['_','_','_','_','_','_']

print(letras_acertadas)
while(not acertou and not enforcou):
    chute=input("Qual a letra? ")
    if chute in palavra_chave:
        posicao=0
        for letra in palavra_chave:
            if chute.upper() == letra.upper():
                print("Encontrou a letra {} na posição {}".format(letra,posicao))
                letras_acertadas[posicao]=letra
            posicao += 1
        acertou = '_' not in letras_acertadas
        enforcou = erros == 6
    else:
        erros += 1
    print(letras_acertadas)


print("Fim do jogo")