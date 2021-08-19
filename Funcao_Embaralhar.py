import random

def embaralhar(palavra):
    vetor = []
    for i in range(len(palavra)):
        vetor = vetor + [palavra[i]]
    
    print("Palavra: ", end='')
    for j in range(len(palavra)):
        print(vetor[j], end='')
    
    random.shuffle(vetor)  
    print("\nEmbaralhada: ", end='')
    for k in range(len(palavra)):
        print(vetor[k], end='')


dig = str(input("Digite uma palavra: "))
embaralhar(dig)