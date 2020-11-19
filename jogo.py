def abertura():
    print("""
    --------------------Jogo da Adivinhação-----------------------
    
    -------------------Escolha a dificuldade----------------------
    """)

n=37
i=0
tentativas=0
chute=0
abertura()
print("1-Facil")
print("2-Normal")
print("3-Dificil")
nivel=int(input("-->"))
if nivel == 1:
    print("Adivinhe o numero de 0 a 100")
    tentativas = 20
    i = tentativas
elif nivel == 2:
    print("Adivinhe o numero de 0 a 100")
    tentativas = 10
    i = tentativas
elif nivel == 3:
    print("Adivinhe o numero de 0 a 100")
    tentativas = 5
    i = tentativas
else:
    print("Opção inválida!")
    exit()
for tentativas in range(1,i+1):
    print("Voce possui {} tentativas".format(i))
    number=int(input("Digite o valor...."))
    i -= 1
    if number == n:
        print("Voce acertou!")
        break
    elif number > 100:
        print("Valor inválido!")
        break
    else:
        print("Voce errou!")
        if i==0:
            print("Acabaram as tentativas voce perdeu")
