a=int(input("Digite o primeiro valor: "))
b=int(input("Digite o segundo valor: "))
c=int(input("Digite o terceiro valor: "))
if (a<b+c) and (b<a+c) and (c<a+b):
    if (b==c) and (a==c):
        print("Triângulo Equilátero ")
    elif (a==b) or (b==c) or (a==c):
        print("Triângulo Isóceles ")
    else:
        print("Triângulo Escaleno ")
else:
    print("Não é possivel formar um triângulo! ")