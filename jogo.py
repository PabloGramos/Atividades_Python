def abertura():
    print("""
    --------------------Jogo da Adivinhação-----------------------
    
    ----------------Adivinhe o numero de 0 a 10-------------------
    """)

n=7
i=4
tentativas=4
chute=0
abertura()
for tentativas in range(1,5):
    print("Voce possui {} tentativas".format(i))
    number=int(input("Digite o valor...."))
    i -= 1
    if number == n:
        print("Voce acertou!")
        break
    elif number > 10:
        print("Valor inválido!")
        break
    else:
        print("Voce errou!")
        if i==0:
            print("Acabaram as tentativas voce perdeu")