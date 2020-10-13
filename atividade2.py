frequencia = float(input("Frequencia em %: "))

if frequencia >= 75:
    print("Sem problemas em frequencia...")
else:
    print("Reprovado por auzencia")


media = float(input("Nota média: "))

if media <= 3:
    print ("Reprovado")
elif media <= 7:
    print("Exame")
elif media <= 10:
    print("Aprovado")
else:
    print("Reprovado")