media=0
quantatual=int(input("Digite a quantidade atual em estoque: "))
quantmax=int(input("Digite a quantidade maxima de estoque: "))
quantmin=int(input("Digite a quantidade minima de estoque: "))
media=(quantmax+quantmin)/2
if quantatual >= media:
    print("Não efetuar compra! ")
else:
    print("Efetuar compra. ")