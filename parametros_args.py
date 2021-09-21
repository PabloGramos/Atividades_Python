def lados_triangulo(*args):
    lista = []
    for valor in args:
        lista.append(valor)

    if lista[0] == lista[1] == lista[2]:
        print("\nO triângulo é Equilátero")
    
    elif lista[0] == lista[1] != lista[2] or lista[1] == lista[0] != lista[2] or lista[2] == lista[0] != lista[1] or lista[2] == lista[1] != lista[0]:
        print("\nO triângulo é Isósceles")
    
    else:
        print("\nO triângulo é Escaleno")




print("Tipo do Triângulo pela medida dos lados...\n")

val1 = int(input("Digite o valor do 1 lado: "))
val2 = int(input("Digite o valor do 2 lado: "))
val3 = int(input("Digite o valor do 3 lado: "))

lados_triangulo(val1, val2, val3)

    
