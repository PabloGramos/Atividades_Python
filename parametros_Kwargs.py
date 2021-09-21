def triangulo_angulos(**kwargs):
    if kwargs['a1'] == 90 or kwargs['a2'] == 90 or kwargs['a3'] == 90:
        print("\nO triângulo é um Triângulo Retângulo")

    elif kwargs['a1'] > 90 or kwargs['a2'] > 90 or kwargs['a3'] > 90:
        print("\nO triângulo é um Triângulo Obtusângulo")

    elif kwargs['a1'] < 90 and kwargs['a2'] < 90 and kwargs['a3'] < 90:
        print("\nO triângulo é um Triângulo Acutângulo")




print("Tipo do Triângulo pelo ângulo...\n")

ang1 = int(input("Digite o 1 ângulo: "))
ang2 = int(input("Digite o 2 ângulo: "))
ang3 = int(input("Digite o 3 ângulo: "))
kwargs = {'a1':ang1 , 'a2':ang2 , 'a3':ang3}

triangulo_angulos(**kwargs)
