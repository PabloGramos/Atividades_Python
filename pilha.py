def main():
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reversa = []
    pilha = []
    topo = 0
    soma = 0
    
    for elemento in seq:
        pilha.append(elemento)
        
    print("Pilha: ", pilha)
    
    while len(pilha) > 0:
        topo = pilha.pop()
        reversa.append(topo)
        soma += topo


    print("Pilha Reversa: ", reversa)
    print("\nSoma reversa: ", soma)


main()