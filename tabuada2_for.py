valor = int(input('Digite um número para saber a tabuada: '))
c = 0
n1=int(input("Número inicial: "))
n2=int(input("Número final: "))
print('-' * 18)
print('Tabuada de {}'.format(valor))
print('-' * 18)
print("Vou fazer a tabuada de {} começando em {} e terminando em {}: ".format(valor, n1, n2))
for c in range(n1,n2+1):
  print('{} X {} = {}'.format(c, valor, (c * valor)))
  c = c + 1
